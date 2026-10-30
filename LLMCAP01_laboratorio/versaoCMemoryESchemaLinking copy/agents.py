import re
import json
import uuid
import sqlite3
import httpx
from fastapi import HTTPException
from pydantic import BaseModel, Field
from typing import Literal, Dict, List, Any, Optional

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODELO_LLM = "llama3.2:1b"


# -------------------------------------------------------------
# SCHEMAS DE DADOS (Pydantic)
# -------------------------------------------------------------
class AnaliseDialogoExtraida(BaseModel):
    pertinente_ao_banco: bool = True
    precisa_clarificacao: bool = False
    pergunta_clarificacao: str = ""
    pergunta_reescrita: str = ""
    categoria: Literal["MANUTENCAO_ELETRICA", "LOGISTICA", "FATURAMENTO", "OUTRO"] = "OUTRO"
    prioridade: Literal["BAIXA", "MEDIA", "ALTA", "CRITICA"] = "MEDIA"
    equipamento_afetado: str = Field(default="NENHUM")
    local_afetado: str = Field(default="NÃO INFORMADO")
    descricao_resumida: str = Field(default="")


# -------------------------------------------------------------
# 1. SESSION MEMORY (Memória Conversacional por Session ID)
# -------------------------------------------------------------
class SessionMemory:
    """
    Gerencia o histórico conversacional por session_id para permitir
    clarificação de dados faltantes em múltiplos turnos de conversa.
    """
    def __init__(self):
        self.sessoes: Dict[str, List[str]] = {}

    def obter_ou_criar_sessao(self, session_id: Optional[str] = None) -> str:
        if not session_id or session_id not in self.sessoes:
            novo_id = session_id or str(uuid.uuid4())[:8]
            self.sessoes[novo_id] = []
            return novo_id
        return session_id

    def adicionar_mensagem(self, session_id: str, autor: str, texto: str):
        if session_id not in self.sessoes:
            self.sessoes[session_id] = []
        self.sessoes[session_id].append(f"{autor}: {texto}")
        # Mantém os últimos 6 turnos na memória
        if len(self.sessoes[session_id]) > 6:
            self.sessoes[session_id] = self.sessoes[session_id][-6:]

    def recuperar_historico(self, session_id: str) -> List[str]:
        return self.sessoes.get(session_id, [])

    def recuperar_historico_texto(self, session_id: str) -> str:
        return "\n".join(self.recuperar_historico(session_id))

    def limpar_sessao(self, session_id: str):
        if session_id in self.sessoes:
            self.sessoes[session_id] = []


# -------------------------------------------------------------
# 2. SCHEMA LINKING TOOL (Mapeamento Determinístico para o ERP)
# -------------------------------------------------------------
class SchemaLinkingTool:
    """
    Traduz termos de negócio para categorias do ERP e extrai evidências.
    """
    def __init__(self):
        self.mapa = {
            "MANUTENCAO_ELETRICA": [
                "transformador", "energia", "disjuntor", "subestação",
                "subestacao", "motor", "cabo", "painel", "fumaça",
                "fumaca", "curto circuito", "chave", "religador", "tr-", "dj-"
            ],
            "LOGISTICA": [
                "entrega", "frete", "transporte", "estoque", "rota", "pedido"
            ],
            "FATURAMENTO": [
                "fatura", "boleto", "pagamento", "financeiro", "nota", "duplicata"
            ]
        }

    def identificar_categoria(self, texto: str) -> Dict[str, Any]:
        texto_lower = (texto or "").lower()
        for categoria, palavras in self.mapa.items():
            encontradas = [p for p in palavras if p in texto_lower]
            if encontradas:
                return {
                    "categoria": categoria,
                    "evidencias": encontradas
                }
        return {
            "categoria": "OUTRO",
            "evidencias": []
        }


# -------------------------------------------------------------
# 3. FUNÇÕES AUXILIARES DE LIMPEZA E NORMALIZAÇÃO
# -------------------------------------------------------------
def extrair_json_resiliente(texto: str) -> dict:
    texto = (texto or "").strip()
    if texto.startswith("```"):
        texto = re.sub(r"^```(?:json)?\s*", "", texto, flags=re.I)
        texto = re.sub(r"\s*```\s*$", "", texto, flags=re.I)
    match = re.search(r"\{.*\}", texto, flags=re.S)
    if match:
        texto = match.group(0)
    try:
        return json.loads(texto)
    except Exception:
        return {}


def normalizar_categoria(categoria: str | None) -> str:
    if not categoria:
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
    if "MANUTENCAO" in valor or "ELETR" in valor:
        return "MANUTENCAO_ELETRICA"
    return "OUTRO"


def normalizar_prioridade(prioridade: str | None, texto_contexto: str = "") -> str:
    texto_lower = texto_contexto.lower()
    # Heurística de segurança operacional: fumaça, fogo, hospital ou explosão elevam a prioridade
    if any(k in texto_lower for k in ["hospital", "fumaça", "fumaca", "fogo", "explosão", "curto"]):
        return "CRITICA"

    if not prioridade:
        return "MEDIA"
    valor = str(prioridade).strip().upper().replace("-", "_").replace(" ", "_")
    if valor.startswith("CRIT"):
        return "CRITICA"
    if valor.startswith("ALT"):
        return "ALTA"
    if valor.startswith("BAIX"):
        return "BAIXA"
    return "MEDIA"


def extrair_equipamento_heuristica(texto: str, valor_llm: str) -> str:
    # Procura códigos técnicos padrão (ex: TR-02, DJ-102, CH-04, SE-BTL)
    padrao = re.search(r"\b(TR-\d+|DJ-\d+|CH-\d+|AL-\d+|transformador\s+\w+|disjuntor\s+\w+)\b", texto, flags=re.I)
    if padrao:
        return padrao.group(0).upper()
    val = str(valor_llm or "").strip()
    if val.upper() not in {"", "NENHUM", "NONE", "NULL", "NÃO INFORMADO", "NAO INFORMADO", "NOME DO EQUIPAMENTO OU NENHUM"}:
        return val
    return "NENHUM"


def extrair_local_heuristica(texto: str, valor_llm: str) -> str:
    padrao = re.search(r"\b(subestação\s+\w+|subestacao\s+\w+|se-\w+|centro|ahu|batel|cic|regional\s+\w+)\b", texto, flags=re.I)
    if padrao:
        return padrao.group(0).title()
    val = str(valor_llm or "").strip()
    if val.upper() not in {"", "NENHUM", "NONE", "NULL", "NÃO INFORMADO", "NAO INFORMADO", "LOCAL OU NAO INFORMADO"}:
        return val
    return "NÃO INFORMADO"


# -------------------------------------------------------------
# 4. DIALOGUE CONTROL AGENT (Orquestrador Cognitivo)
# -------------------------------------------------------------
class DialogueControlAgent:
    """
    Controla o diálogo multi-turno, combina o histórico da SessionMemory
    com o SchemaLinkingTool e decide se pede clarificação ou grava a OS.
    """
    def __init__(self, memory: SessionMemory, schema_tool: SchemaLinkingTool):
        self.memory = memory
        self.schema_tool = schema_tool

    async def processar_interacao(
        self, session_id: Optional[str], cliente_id: int, texto_mensagem: str
    ) -> Dict[str, Any]:
        # 1. Obtém ou cria a sessão na memória e adiciona o relato do usuário
        sid = self.memory.obter_ou_criar_sessao(session_id)
        self.memory.adicionar_mensagem(sid, "Operador", texto_mensagem)

        # 2. Recupera todo o histórico acumulado da conversa
        historico_lista = self.memory.recuperar_historico(sid)
        historico_texto = "\n".join(historico_lista)

        # 3. Passa o contexto acumulado pelo Schema Linking Tool
        contexto_schema = self.schema_tool.identificar_categoria(historico_texto)

        # 4. Invoca a LLM para interpretar e extrair dados estruturados
        analise = await self._interpretar_com_llm(
            texto_atual=texto_mensagem,
            historico_texto=historico_texto,
            contexto_schema=contexto_schema
        )

        return {
            "session_id": sid,
            "analise": analise,
            "contexto_schema": contexto_schema,
            "historico_sessao": historico_lista
        }

    async def _interpretar_com_llm(
        self, texto_atual: str, historico_texto: str, contexto_schema: dict
    ) -> AnaliseDialogoExtraida:
        system_prompt = (
            "Voce e um assistente de triagem tecnica de energia eletrica e ERP. "
            "Analise o Historico da Conversa e extraia os dados em formato JSON puro:\n"
            "{\n"
            '  "categoria": "MANUTENCAO_ELETRICA" | "LOGISTICA" | "FATURAMENTO" | "OUTRO",\n'
            '  "prioridade": "BAIXA" | "MEDIA" | "ALTA" | "CRITICA",\n'
            '  "equipamento_afetado": "codigo do equipamento (ex: TR-02, DJ-102) ou NENHUM",\n'
            '  "local_afetado": "nome da subestacao/local (ex: Subestacao Ahu, Centro) ou NAO INFORMADO",\n'
            '  "descricao_resumida": "resumo consolidado do problema em ate 120 caracteres"\n'
            "}\n"
            "Responda APENAS o JSON."
        )

        prompt = f"""Contexto Schema Linking:
Categoria sugerida: {contexto_schema['categoria']}
Evidencias encontradas: {', '.join(contexto_schema['evidencias'])}

Historico acumulado da sessao:
{historico_texto}

Mensagem atual:
{texto_atual}

JSON:"""

        payload = {
            "model": MODELO_LLM,
            "prompt": f"{system_prompt}\n\n{prompt}",
            "format": "json",
            "stream": False
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(OLLAMA_API_URL, json=payload)
                if response.status_code != 200:
                    raise HTTPException(status_code=502, detail=f"Erro no Ollama: {response.text}")

                dados_resposta = response.json()
                texto_json = dados_resposta.get("response", "{}")
                dados_dict = extrair_json_resiliente(texto_json)

                # Consolidação com Schema Linking e Heurísticas determinísticas
                cat_llm = normalizar_categoria(dados_dict.get("categoria"))
                cat_schema = contexto_schema["categoria"]
                categoria_final = cat_schema if cat_schema != "OUTRO" else cat_llm

                prioridade_final = normalizar_prioridade(dados_dict.get("prioridade"), historico_texto)
                equipamento_final = extrair_equipamento_heuristica(historico_texto, dados_dict.get("equipamento_afetado", ""))
                local_final = extrair_local_heuristica(historico_texto, dados_dict.get("local_afetado", ""))

                # Reescrita contextual unindo os turnos da conversa
                mensagens_operador = [
                    m.replace("Operador: ", "")
                    for m in historico_texto.split("\n")
                    if m.startswith("Operador: ")
                ]
                reescrita = " | ".join(mensagens_operador) if len(mensagens_operador) > 1 else ""
                resumo_final = str(dados_dict.get("descricao_resumida") or reescrita or texto_atual)[:120]

                # Verifica pertinência e necessidade de clarificação (campos obrigatórios)
                pertinente = categoria_final != "OUTRO" or equipamento_final != "NENHUM"
                faltando = []
                if equipamento_final == "NENHUM":
                    faltando.append("qual é o código do equipamento afetado (ex: TR-02, DJ-102)")
                if local_final == "NÃO INFORMADO":
                    faltando.append("qual é a Subestação ou localidade da ocorrência")

                precisa_clarificacao = len(faltando) > 0
                pergunta_clar = ""
                if precisa_clarificacao:
                    pergunta_clar = (
                        f"Entendi o relato ({categoria_final}). Para registrar a Ordem de Serviço no ERP, "
                        f"por favor informe {' e '.join(faltando)}."
                    )

                return AnaliseDialogoExtraida(
                    pertinente_ao_banco=pertinente,
                    precisa_clarificacao=precisa_clarificacao,
                    pergunta_clarificacao=pergunta_clar,
                    pergunta_reescrita=reescrita,
                    categoria=categoria_final,
                    prioridade=prioridade_final,
                    equipamento_afetado=equipamento_final,
                    local_afetado=local_final,
                    descricao_resumida=resumo_final
                )

        except httpx.ConnectError:
            raise HTTPException(
                status_code=503,
                detail="O Ollama nao esta em execucao. Inicie-o com 'ollama serve' no terminal."
            )
        except Exception as e:
            raise HTTPException(status_code=422, detail=f"Falha no processamento cognitivo: {str(e)}")


# -------------------------------------------------------------
# 5. TICKET AGENT / TEXT-TO-SQL TOOL (Persistência SQLite)
# -------------------------------------------------------------
class TicketAgent:
    """
    Executa a persistência determinística e segura no banco SQLite do ERP.
    """
    def __init__(self, db_path: str = "erp_simulado.db"):
        self.db_path = db_path
        self.init_erp_db()

    def init_erp_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ordens_servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER,
                categoria TEXT,
                prioridade TEXT,
                equipamento TEXT,
                local TEXT DEFAULT 'NÃO INFORMADO',
                descricao_resumida TEXT,
                status TEXT DEFAULT 'ABERTA'
            )
        """)
        # Garante que a coluna 'local' exista mesmo se o arquivo .db foi criado na versão antiga
        cursor.execute("PRAGMA table_info(ordens_servico)")
        colunas = [col[1] for col in cursor.fetchall()]
        if "local" not in colunas:
            cursor.execute("ALTER TABLE ordens_servico ADD COLUMN local TEXT DEFAULT 'NÃO INFORMADO'")
        conn.commit()
        conn.close()

    def criar_ordem_servico(self, cliente_id: int, analise: AnaliseDialogoExtraida) -> int:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ordens_servico (cliente_id, categoria, prioridade, equipamento, local, descricao_resumida)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            cliente_id,
            analise.categoria,
            analise.prioridade,
            analise.equipamento_afetado,
            analise.local_afetado,
            analise.descricao_resumida
        ))
        os_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return os_id

    def listar_ordens_servico(self) -> List[Dict[str, Any]]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, cliente_id, categoria, prioridade, equipamento, local, descricao_resumida, status FROM ordens_servico ORDER BY id DESC")
        linhas = cursor.fetchall()
        conn.close()
        return [
            {
                "id": l[0],
                "cliente_id": l[1],
                "categoria": l[2],
                "prioridade": l[3],
                "equipamento": l[4],
                "local": l[5] or "NÃO INFORMADO",
                "descricao": l[6],
                "status": l[7]
            }
            for l in linhas
        ]
