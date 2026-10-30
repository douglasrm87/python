# Para poder executar

    # pip install fastapi uvicorn httpx pydantic
#Caso já tenha o Ollama instalado em sua máquina: ollama run llama3.2:1b
    # Instalar se não tiver: curl -fsSL https://ollama.com/install.sh | sh
    #  iniciar o daemon em background (ollama serve &) 
#Inicie o servidor Backend: python server.py


import os
import re
import sqlite3
import json
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(title="Laboratorio ADS - Integracao LLM e ERP")


@app.get("/", include_in_schema=False)
async def home():
    return FileResponse("home.html")


@app.get("/triagem", include_in_schema=False)
async def pagina_triagem():
    return FileResponse("index.html")


# Habilita CORS para permitir que o arquivo index.html converse com este backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------
# 1. BANCO DE DADOS ERP SIMULADO (SQLite em Memória)
# -------------------------------------------------------------
def init_erp_db():
    conn = sqlite3.connect("erp_simulado.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ordens_servico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            categoria TEXT,
            prioridade TEXT,
            equipamento TEXT,
            descricao_resumida TEXT,
            status TEXT DEFAULT 'ABERTA'
        )
    """)
    conn.commit()
    conn.close()

init_erp_db()

# -------------------------------------------------------------
# 2. SCHEMAS DE DADOS (Pydantic)
# -------------------------------------------------------------
class MensagemClienteRequest(BaseModel):
    cliente_id: int
    texto_mensagem: str

class OrdemServicoExtraida(BaseModel):
    categoria: Literal["MANUTENCAO_ELETRICA", "LOGISTICA", "FATURAMENTO", "OUTRO"]
    prioridade: Literal["BAIXA", "MEDIA", "ALTA", "CRITICA"]
    equipamento_afetado: str = Field(description="Nome do equipamento ou 'NENHUM'")
    descricao_resumida: str = Field(description="Resumo claro do problema em ate 120 caracteres")

# -------------------------------------------------------------
# 3. CONEXÃO COM O LLM LOCAL (Ollama)
# -------------------------------------------------------------
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODELO_LLM = "llama3.2:1b"


def normalizar_categoria(categoria: str | None) -> str:
    if categoria is None:
        return "OUTRO"
    valor = str(categoria).strip().upper().replace("-", "_").replace(" ", "_")
    aliases = {
        "MANUTENCAO_ELETRICA": "MANUTENCAO_ELETRICA",
        "MANUTENCAEIRA": "MANUTENCAO_ELETRICA",
        "MANUTENCAO_ELETRIC": "MANUTENCAO_ELETRICA",
        "ELETRICA": "MANUTENCAO_ELETRICA",
        "LOGISTICA": "LOGISTICA",
        "FATURAMENTO": "FATURAMENTO",
        "OUTRO": "OUTRO",
    }
    if valor in aliases:
        return aliases[valor]
    if "MANUTENCAO" in valor and ("ELETR" in valor or "ELETR" in valor):
        return "MANUTENCAO_ELETRICA"
    return "OUTRO" if valor not in {"MANUTENCAO_ELETRICA", "LOGISTICA", "FATURAMENTO", "OUTRO"} else valor


def normalizar_prioridade(prioridade: str | None) -> str:
    if prioridade is None:
        return "MEDIA"
    valor = str(prioridade).strip().upper().replace("-", "_").replace(" ", "_")
    aliases = {
        "BAIXA": "BAIXA",
        "MEDIA": "MEDIA",
        "MÉDIA": "MEDIA",
        "ALTA": "ALTA",
        "CRITICA": "CRITICA",
        "CRITICO": "CRITICA",
    }
    if valor in aliases:
        return aliases[valor]
    if valor.startswith("CRIT"):
        return "CRITICA"
    if valor.startswith("ALT"):
        return "ALTA"
    if valor.startswith("MED"):
        return "MEDIA"
    if valor.startswith("BAIX"):
        return "BAIXA"
    return "MEDIA"


def classificar_categoria_por_palavras(texto: str) -> str:
    texto_lower = (texto or "").lower()
    if any(p in texto_lower for p in [
        "transformador", "disjuntor", "subestação", "energia", "eletrica", "elétrica",
        "motor", "cabo", "queda de energia", "fumaça", "curto circuito", "painel"
    ]):
        return "MANUTENCAO_ELETRICA"
    if any(p in texto_lower for p in [
        "entrega", "estoque", "transporte", "frete", "rotas", "logistica", "pedido"
    ]):
        return "LOGISTICA"
    if any(p in texto_lower for p in [
        "fatura", "nota", "boleto", "cobrança", "financeiro", "duplicata", "pagamento"
    ]):
        return "FATURAMENTO"
    return "OUTRO"


def extrair_json_do_texto(texto: str) -> dict:
    texto = texto.strip()
    if texto.startswith("```"):
        texto = re.sub(r"^```(?:json)?\s*", "", texto, flags=re.I)
        texto = re.sub(r"\s*```\s*$", "", texto, flags=re.I)
    match = re.search(r"\{.*\}", texto, flags=re.S)
    if match:
        texto = match.group(0)
    return json.loads(texto)


async def extrair_com_llm(texto_mensagem: str) -> OrdemServicoExtraida:
    """
    Envia a mensagem ao modelo e exige um JSON estruturado estrito.
    """
    system_prompt = (
        "Voce e um assistente especializado em triagem tecnica industrial e ERP. "
        "Sua unica tarefa e analisar o relato do cliente e preencher estritamente um JSON "
        "com o seguinte formato:\n"
        "{\n"
        '  "categoria": "MANUTENCAO_ELETRICA" | "LOGISTICA" | "FATURAMENTO" | "OUTRO",\n'
        '  "prioridade": "BAIXA" | "MEDIA" | "ALTA" | "CRITICA",\n'
        '  "equipamento_afetado": "nome do equipamento ou NENHUM",\n'
        '  "descricao_resumida": "resumo claro do problema em ate 120 caracteres"\n'
        "}\n"
        "IMPORTANTE: Nao adicione introducoes, explicacoes ou crases de markdown. "
        "Responda apenas o objeto JSON puro."
    )

    prompt = f"Relato do cliente:\n{texto_mensagem}\n\nJSON:"

    payload = {
        "model": MODELO_LLM,
        "prompt": f"{system_prompt}\n\n{prompt}",
        "format": "json",  # Garante saida restrita a JSON
        "stream": False
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(OLLAMA_API_URL, json=payload)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=502, 
                    detail=f"Erro no Ollama: {response.text}"
                )
            dados_resposta = response.json()
            texto_json = dados_resposta.get("response", "{}")

            dados_dict = extrair_json_do_texto(texto_json)
            categoria = normalizar_categoria(dados_dict.get("categoria"))
            if categoria == "OUTRO":
                categoria = classificar_categoria_por_palavras(texto_mensagem)
            dados_dict["categoria"] = categoria
            dados_dict["prioridade"] = normalizar_prioridade(dados_dict.get("prioridade"))
            dados_dict["equipamento_afetado"] = str(dados_dict.get("equipamento_afetado", "NENHUM") or "NENHUM")
            dados_dict["descricao_resumida"] = str(dados_dict.get("descricao_resumida", "") or "")[:120]

            return OrdemServicoExtraida(**dados_dict)
    except httpx.ConnectError:
        raise HTTPException(
            status_code=503,
            detail="O Ollama nao esta em execucao. Inicie-o com 'ollama serve' no terminal."
        )
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Falha na extracao/validacao dos dados: {str(e)}")

# -------------------------------------------------------------
# 4. ENDPOINT DA APLICAÇÃO
# -------------------------------------------------------------
@app.post("/api/chamados/processar")
async def processar_chamado(requisicao: MensagemClienteRequest):
    # Passo 1: LLM interpreta o texto
    os_extraida = await extrair_com_llm(requisicao.texto_mensagem)

    # Passo 2: Backend insere no ERP de forma determinística e segura
    conn = sqlite3.connect("erp_simulado.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ordens_servico (cliente_id, categoria, prioridade, equipamento, descricao_resumida)
        VALUES (?, ?, ?, ?, ?)
    """, (
        requisicao.cliente_id,
        os_extraida.categoria,
        os_extraida.prioridade,
        os_extraida.equipamento_afetado,
        os_extraida.descricao_resumida
    ))
    os_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return {
        "status": "SUCESSO",
        "ordem_servico_id": os_id,
        "dados_gerados": os_extraida.model_dump(),
        "mensagem": f"Ordem de Servico #{os_id} aberta com sucesso no ERP."
    }

@app.get("/api/chamados")
def listar_chamados():
    conn = sqlite3.connect("erp_simulado.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ordens_servico ORDER BY id DESC")
    linhas = cursor.fetchall()
    conn.close()
    return [{"id": l[0], "cliente_id": l[1], "categoria": l[2], "prioridade": l[3], "equipamento": l[4], "descricao": l[5], "status": l[6]} for l in linhas]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
