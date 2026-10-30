"""
LLMCAP01_laboratorio/server.py
Implementação Modular Resiliente: Dialogue Control Agent + Text-to-SQL Agent
Com auto-detecção de modelo Ollama e fallback seguro contra erros de modelo inexistente.
"""

import json
import os
import re
import sqlite3
from typing import Dict, List, Literal, Optional
from uuid import uuid4

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

# ==============================================================================
# 1. CONFIGURAÇÕES E BANCO DE DADOS ERP SIMULADO
# ==============================================================================
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODELO_LLM_PREFERENCIAL = os.getenv("MODELO_LLM", "llama3.2:1b")

app = FastAPI(
    title="Laboratório ADS - Dialogue Control Agent & Text-to-SQL",
    description="Implementação modular resiliente baseada no padrão Dialogue Interfaces"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
            subestacao_local TEXT,
            descricao_resumida TEXT,
            status TEXT DEFAULT 'ABERTA'
        )
    """)
    conn.commit()
    conn.close()

init_erp_db()

# ==============================================================================
# 2. CONTRATOS DE DADOS (SCHEMAS PYDANTIC)
# ==============================================================================
class MensagemChatRequest(BaseModel):
    session_id: Optional[str] = Field(default=None, description="Identificador da sessão")
    cliente_id: int = Field(default=1042, description="ID do usuário/técnico")
    texto_mensagem: str = Field(..., min_length=1, description="Texto digitado pelo usuário")

class AvaliacaoDialogueAgent(BaseModel):
    pertinente_ao_banco: bool = Field(
        default=True,
        description="Regra 1: True se a mensagem for sobre chamados, equipamentos ou operações"
    )
    precisa_reescrever: bool = Field(
        default=False,
        description="Regra 2: True se a mensagem contiver termos ambíguos ou depender do histórico"
    )
    pergunta_reescrita: Optional[str] = Field(
        default=None,
        description="Regra 2: Pergunta enriquecida com dados da sessão para a ferramenta de SQL"
    )
    precisa_clarificacao: bool = Field(
        default=False,
        description="Regra 4: True se faltarem dados essenciais (equipamento/local)"
    )
    pergunta_clarificacao: Optional[str] = Field(
        default=None,
        description="Pergunta educada ao técnico solicitando o dado faltante"
    )
    categoria: Literal["MANUTENCAO_ELETRICA", "LOGISTICA", "FATURAMENTO", "OUTRO"] = "MANUTENCAO_ELETRICA"
    prioridade: Literal["BAIXA", "MEDIA", "ALTA", "CRITICA"] = "MEDIA"
    equipamento_afetado: str = Field(default="NENHUM")
    subestacao_local: str = Field(default="NAO_INFORMADO")
    descricao_resumida: str = Field(default="")

class RespostaChat(BaseModel):
    session_id: str
    tipo_resposta: Literal[
        "CONVERSA_GERAL",
        "PERGUNTA_CLARIFICACAO",
        "ORDEM_CRIADA",
        "ERRO_AMIGAVEL"
    ]
    mensagem_assistente: str
    ordem_servico_id: Optional[int] = None
    pergunta_reescrita_usada: Optional[str] = None
    dados_estruturados: Optional[dict] = None

# ==============================================================================
# 3. MÓDULO DE MEMÓRIA DE SESSÃO (SESSION MEMORY)
# ==============================================================================
class SessionMemory:
    def __init__(self):
        self._sessoes: Dict[str, List[Dict[str, str]]] = {}

    def get_ou_criar(self, session_id: Optional[str]) -> str:
        if not session_id or session_id not in self._sessoes:
            novo_id = session_id or str(uuid4())[:8]
            self._sessoes[novo_id] = []
            return novo_id
        return session_id

    def adicionar(self, session_id: str, papel: str, conteudo: str):
        if session_id in self._sessoes:
            self._sessoes[session_id].append({"role": papel, "content": conteudo})

    def obter_historico_formatado(self, session_id: str) -> str:
        mensagens = self._sessoes.get(session_id, [])
        if not mensagens:
            return "Nenhum histórico anterior."
        linhas = []
        for m in mensagens:
            prefixo = "Técnico" if m["role"] == "user" else "Assistente"
            linhas.append(f"{prefixo}: {m['content']}")
        return "\n".join(linhas)

memoria_global = SessionMemory()

# ==============================================================================
# 4. SANITIZAÇÃO DEFENSIVA E RESOLUÇÃO DE MODELO
# ==============================================================================
def extrair_json_resiliente(texto: str) -> dict:
    texto = texto.strip()
    if texto.startswith("```"):
        texto = re.sub(r"^```(?:json)?\s*", "", texto, flags=re.I)
        texto = re.sub(r"\s*```\s*$", "", texto, flags=re.I)
    match = re.search(r"\{.*\}", texto, flags=re.DOTALL)
    if match:
        texto = match.group(0)
    return json.loads(texto)

def normalizar_categoria(cat: Optional[str], texto_contexto: str) -> str:
    aliases = {
        "MANUTENCAO_ELETRICA": "MANUTENCAO_ELETRICA",
        "ELETRICA": "MANUTENCAO_ELETRICA",
        "LOGISTICA": "LOGISTICA",
        "FATURAMENTO": "FATURAMENTO",
    }
    limpo = str(cat or "").strip().upper().replace(" ", "_").replace("-", "_")
    if limpo in aliases:
        return aliases[limpo]
    t_low = texto_contexto.lower()
    if any(k in t_low for k in ["transformador", "disjuntor", "fumaça", "curto", "subestação", "rede", "óleo", "chave", "alimentador", "trafo", "dj", "al"]):
        return "MANUTENCAO_ELETRICA"
    if any(k in t_low for k in ["entrega", "caminhão", "frete", "rota"]):
        return "LOGISTICA"
    if any(k in t_low for k in ["nota", "fatura", "boleto", "pagamento"]):
        return "FATURAMENTO"
    return "OUTRO"

def normalizar_prioridade(prio: Optional[str]) -> str:
    limpo = str(prio or "").strip().upper()
    if limpo.startswith("CRIT") or "URGENTE" in limpo or "FOGO" in limpo: return "CRITICA"
    if limpo.startswith("ALT"): return "ALTA"
    if limpo.startswith("BAIX"): return "BAIXA"
    return "MEDIA"

async def resolver_modelo_disponivel(base_url: str, preferencial: str) -> str:
    """Verifica os modelos presentes no Ollama e seleciona o melhor disponível."""
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            res = await client.get(f"{base_url}/api/tags")
            if res.status_code == 200:
                modelos = [m.get("name", "") for m in res.json().get("models", [])]
                if preferencial in modelos:
                    return preferencial
                for m in modelos:
                    if preferencial.split(":")[0] in m:
                        return m
                if modelos:
                    return modelos[0]
    except Exception:
        pass
    return preferencial

# ==============================================================================
# 5. AGENTE 1: DIALOGUE CONTROL AGENT
# ==============================================================================
class DialogueControlAgent:
    def __init__(self, base_url: str, default_model: str):
        self.base_url = base_url
        self.default_model = default_model

    async def avaliar_dialogo(self, historico: str, mensagem: str) -> AvaliacaoDialogueAgent:
        system_prompt = (
            "# You are a Dialogue Control Agent that manages user questions about an ERP database for company operations.\n\n"
            "# Glossário e Sinônimos Operacionais da Empresa (ADMS / Gestão de Campo):\n"
            "- 'AL' ou 'Alimentador' (ex: AL-03, AL-NORTE): Linha de média tensão de distribuição.\n"
            "- 'DJ' ou 'Disjuntor': Equipamento de manobra e proteção automática da subestação.\n"
            "- 'Trafo', 'TR' ou 'Transformador' (ex: TR-02): Ativo de transformação de tensão.\n"
            "- 'Chave Faca' ou 'Chave Tandem': Mapear para equipamento 'Seccionadora Monopolar'.\n"
            "- '50/51': Atuação por sobrecorrente de fase/neutro (Manutenção Elétrica de Alta Prioridade).\n"
            "- '86': Relé de bloqueio (exige inspeção presencial antes de reenergizar).\n"
            "- 'Padrão P-3' ou 'Padrão P-13': Mapear como infraestrutura de medição de entrada de consumidor.\n\n"
            "# Rules:\n"
            "1. First, verify if the question is about the database (equipment, service orders, electrical maintenance, logistics, billing).\n"
            "2. If it is, decide if the question needs to be rewritten.\n"
            "   - If yes (e.g., user says 'it', 'there', or adds partial info), enrich the question with data from dialogue history.\n"
            "   - Otherwise, use the original question.\n"
            "3. If critical information is missing to register or query the database (e.g. equipment tag or substation), "
            "set precisa_clarificacao = true and formulate a polite clarification question.\n"
            "4. ATTENTION: Do NOT try to convert the question to SQL. Your responsibility is dialogue control and question preparation.\n\n"
            "Respond ONLY a valid JSON object matching this schema:\n"
            "{\n"
            '  "pertinente_ao_banco": true | false,\n'
            '  "precisa_reescrever": true | false,\n'
            '  "pergunta_reescrita": "pergunta enriquecida ou null",\n'
            '  "precisa_clarificacao": true | false,\n'
            '  "pergunta_clarificacao": "pergunta educada ao técnico ou null",\n'
            '  "categoria": "MANUTENCAO_ELETRICA" | "LOGISTICA" | "FATURAMENTO" | "OUTRO",\n'
            '  "prioridade": "BAIXA" | "MEDIA" | "ALTA" | "CRITICA",\n'
            '  "equipamento_afetado": "nome/tag ou NENHUM",\n'
            '  "subestacao_local": "local ou NAO_INFORMADO",\n'
            '  "descricao_resumida": "resumo claro em até 120 caracteres"\n'
            "}"
        )

        user_content = (
            f"Histórico do Diálogo:\n{historico}\n\n"
            f"Mensagem atual do usuário: \"{mensagem}\"\n\nJSON:"
        )

        modelo_ativo = await resolver_modelo_disponivel(self.base_url, self.default_model)

        payload = {
            "model": modelo_ativo,
            "prompt": f"{system_prompt}\n\n{user_content}",
            "format": "json",
            "stream": False
        }

        try:
            async with httpx.AsyncClient(timeout=25.0) as client:
                res = await client.post(f"{self.base_url}/api/generate", json=payload)
                if res.status_code == 200:
                    corpo = res.json().get("response", "{}")
                    dados = extrair_json_resiliente(corpo)
                    
                    cat = normalizar_categoria(dados.get("categoria"), f"{historico} {mensagem}")
                    prio = normalizar_prioridade(dados.get("prioridade"))
                    equip = str(dados.get("equipamento_afetado", "NENHUM") or "NENHUM")
                    local = str(dados.get("subestacao_local", "NAO_INFORMADO") or "NAO_INFORMADO")
                    desc = str(dados.get("descricao_resumida", mensagem))[:120]
                    pertinente = bool(dados.get("pertinente_ao_banco", True))
                    clarifica = bool(dados.get("precisa_clarificacao", False))
                    pergunta = dados.get("pergunta_clarificacao")
                    reescrita = dados.get("pergunta_reescrita")

                    if cat == "MANUTENCAO_ELETRICA" and (equip in ["NENHUM", ""] or local in ["NAO_INFORMADO", ""]):
                        clarifica = True
                        if not pergunta:
                            pergunta = "Identifiquei uma ocorrência técnica de manutenção elétrica. Poderia informar o equipamento específico e a subestação/local para abrirmos a OS?"

                    return AvaliacaoDialogueAgent(
                        pertinente_ao_banco=pertinente,
                        precisa_reescrever=bool(dados.get("precisa_reescrever", False)),
                        pergunta_reescrita=reescrita,
                        precisa_clarificacao=clarifica,
                        pergunta_clarificacao=pergunta,
                        categoria=cat,
                        prioridade=prio,
                        equipamento_afetado=equip,
                        subestacao_local=local,
                        descricao_resumida=desc
                    )
        except Exception:
            pass

        # Fallback defensivo determinístico caso o Ollama esteja inacessível ou falhe
        t_low = f"{historico} {mensagem}".lower()
        cat = normalizar_categoria(None, t_low)
        prio = "CRITICA" if any(w in t_low for w in ["fumaça", "fogo", "curto", "urgente"]) else "ALTA"
        
        equip = "Transformador" if "trafo" in t_low or "transformador" in t_low else ("Disjuntor" if "dj" in t_low or "disjuntor" in t_low else "NENHUM")
        local = "Subestação Ahu" if "ahu" in t_low else ("Subestação Batel" if "batel" in t_low else "NAO_INFORMADO")
        precisa_clarificar = (equip == "NENHUM" or local == "NAO_INFORMADO")

        return AvaliacaoDialogueAgent(
            pertinente_ao_banco=True,
            precisa_reescrever=False,
            pergunta_reescrita=None,
            precisa_clarificacao=precisa_clarificar,
            pergunta_clarificacao="Poderia informar qual o equipamento específico e a subestação/local da ocorrência?" if precisa_clarificar else None,
            categoria=cat,
            prioridade=prio,
            equipamento_afetado=equip,
            subestacao_local=local,
            descricao_resumida=mensagem[:120]
        )

# ==============================================================================
# 6. AGENTE 2: TEXT-TO-SQL / ERP SPECIALIST TOOL
# ==============================================================================
class TextToSqlAgent:
    @staticmethod
    def compilar_e_executar_insert(cliente_id: int, dados: AvaliacaoDialogueAgent) -> int:
        conn = sqlite3.connect("erp_simulado.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ordens_servico (
                cliente_id, categoria, prioridade, equipamento, subestacao_local, descricao_resumida
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            cliente_id,
            dados.categoria,
            dados.prioridade,
            dados.equipamento_afetado,
            dados.subestacao_local,
            dados.descricao_resumida
        ))
        os_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return os_id

dialogue_control = DialogueControlAgent(OLLAMA_BASE_URL, MODELO_LLM_PREFERENCIAL)
sql_tool = TextToSqlAgent()

# ==============================================================================
# 7. ENDPOINTS DA API
# ==============================================================================
@app.get("/", include_in_schema=False)
async def home_route():
    if os.path.exists("home.html"):
        return FileResponse("home.html")
    return {"status": "ok", "mensagem": "Arquivo home.html não localizado na pasta raiz."}

@app.get("/triagem", include_in_schema=False)
async def triagem_route():
    if os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"status": "ok", "mensagem": "Arquivo index.html não localizado na pasta raiz."}

@app.post("/api/chat/mensagem", response_model=RespostaChat)
async def processar_mensagem_chat(req: MensagemChatRequest):
    sess_id = memoria_global.get_ou_criar(req.session_id)
    historico = memoria_global.obter_historico_formatado(sess_id)

    memoria_global.adicionar(sess_id, "user", req.texto_mensagem)
    avaliacao = await dialogue_control.avaliar_dialogo(historico, req.texto_mensagem)

    if not avaliacao.pertinente_ao_banco:
        msg = "Olá! Sou o assistente operacional da empresa. Posso ajudar na abertura de ordens de serviço, triagem de manutenções ou dúvidas sobre equipamentos."
        memoria_global.adicionar(sess_id, "assistant", msg)
        return RespostaChat(
            session_id=sess_id,
            tipo_resposta="CONVERSA_GERAL",
            mensagem_assistente=msg,
            dados_estruturados=avaliacao.model_dump()
        )

    if avaliacao.precisa_clarificacao:
        msg_clarificacao = avaliacao.pergunta_clarificacao or (
            "Peço desculpas, mas faltam dados para registro no ERP. Poderia informar o equipamento e a subestação da ocorrência?"
        )
        memoria_global.adicionar(sess_id, "assistant", msg_clarificacao)
        return RespostaChat(
            session_id=sess_id,
            tipo_resposta="PERGUNTA_CLARIFICACAO",
            mensagem_assistente=msg_clarificacao,
            pergunta_reescrita_usada=avaliacao.pergunta_reescrita,
            dados_estruturados=avaliacao.model_dump()
        )

    pergunta_final = avaliacao.pergunta_reescrita or req.texto_mensagem
    os_id = sql_tool.compilar_e_executar_insert(req.cliente_id, avaliacao)

    msg_sucesso = (
        f"Ordem de Serviço #{os_id} aberta com sucesso no ERP!\n"
        f"• Categoria: {avaliacao.categoria}\n"
        f"• Prioridade: {avaliacao.prioridade}\n"
        f"• Equipamento: {avaliacao.equipamento_afetado}\n"
        f"• Local: {avaliacao.subestacao_local}"
    )
    memoria_global.adicionar(sess_id, "assistant", msg_sucesso)

    return RespostaChat(
        session_id=sess_id,
        tipo_resposta="ORDEM_CRIADA",
        mensagem_assistente=msg_sucesso,
        ordem_servico_id=os_id,
        pergunta_reescrita_usada=pergunta_final,
        dados_estruturados=avaliacao.model_dump()
    )

@app.get("/api/chamados")
def listar_chamados():
    conn = sqlite3.connect("erp_simulado.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, cliente_id, categoria, prioridade, equipamento, subestacao_local, descricao_resumida, status 
        FROM ordens_servico ORDER BY id DESC
    """)
    linhas = cursor.fetchall()
    conn.close()
    return [
        {
            "id": l[0], "cliente_id": l[1], "categoria": l[2],
            "prioridade": l[3], "equipamento": l[4], "local": l[5],
            "descricao": l[6], "status": l[7]
        }
        for l in linhas
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)