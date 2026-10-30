from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

from agents import (
    SessionMemory,
    SchemaLinkingTool,
    DialogueControlAgent,
    TicketAgent,
)

app = FastAPI(title="Laboratorio ADS - Dialogue Control Agent, Schema Linking & Text-to-SQL")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------
# 1. INICIALIZAÇÃO DOS AGENTES E MEMÓRIA
# -------------------------------------------------------------
session_memory = SessionMemory()
schema_linking_tool = SchemaLinkingTool()
dialogue_agent = DialogueControlAgent(memory=session_memory, schema_tool=schema_linking_tool)
ticket_agent = TicketAgent(db_path="erp_simulado.db")


# -------------------------------------------------------------
# 2. SCHEMA DE REQUISIÇÃO (Compatível com index.html e cURL)
# -------------------------------------------------------------
class MensagemChatRequest(BaseModel):
    session_id: Optional[str] = None
    cliente_id: Optional[int] = 1042
    texto_mensagem: str


# -------------------------------------------------------------
# 3. ROTAS DAS PÁGINAS HTML
# -------------------------------------------------------------
@app.get("/", include_in_schema=False)
async def home():
    return FileResponse("home.html")


@app.get("/triagem", include_in_schema=False)
async def pagina_triagem():
    return FileResponse("index.html")


# -------------------------------------------------------------
# 4. ENDPOINTS DA API (Atende ao Chat Multi-turno e ao ERP)
# -------------------------------------------------------------
@app.post("/api/chat/mensagem")
@app.post("/api/chamados/processar")
async def processar_mensagem(requisicao: MensagemChatRequest):
    # Executa o DialogueControlAgent (Memória + Schema Linking + LLM)
    resultado = await dialogue_agent.processar_interacao(
        session_id=requisicao.session_id,
        cliente_id=requisicao.cliente_id or 1042,
        texto_mensagem=requisicao.texto_mensagem
    )

    sid = resultado["session_id"]
    analise = resultado["analise"]
    contexto_schema = resultado["contexto_schema"]

    # Caso falte informação obrigatória (ex: equipamento ou local), solicita clarificação!
    if analise.precisa_clarificacao:
        session_memory.adicionar_mensagem(sid, "Assistente", analise.pergunta_clarificacao)
        return {
            "status": "PENDENTE_CLARIFICACAO",
            "session_id": sid,
            "tipo_resposta": "PERGUNTA_CLARIFICACAO",
            "mensagem_assistente": analise.pergunta_clarificacao,
            "pergunta_reescrita_usada": analise.pergunta_reescrita,
            "schema_linking": contexto_schema,
            "dados_estruturados": {
                "pertinente_ao_banco": analise.pertinente_ao_banco,
                "precisa_clarificacao": True,
                "categoria": analise.categoria,
                "prioridade": analise.prioridade,
                "equipamento": analise.equipamento_afetado,
                "local": analise.local_afetado
            }
        }

    # Se todos os dados obrigatórios estão completos, grava no SQLite via TicketAgent!
    os_id = ticket_agent.criar_ordem_servico(
        cliente_id=requisicao.cliente_id or 1042,
        analise=analise
    )

    msg_sucesso = (
        f"Ordem de Serviço #{os_id} registrada com sucesso! "
        f"[Categoria: {analise.categoria} | Equipamento: {analise.equipamento_afetado} | "
        f"Local: {analise.local_afetado} | Prioridade: {analise.prioridade}]"
    )

    # Limpa a memória da sessão após concluir a abertura da Ordem de Serviço
    session_memory.limpar_sessao(sid)

    return {
        "status": "SUCESSO",
        "session_id": sid,
        "tipo_resposta": "ORDEM_CRIADA",
        "ordem_servico_id": os_id,
        "mensagem_assistente": msg_sucesso,
        "mensagem": msg_sucesso,
        "pergunta_reescrita_usada": analise.pergunta_reescrita,
        "schema_linking": contexto_schema,
        "dados_gerados": analise.model_dump(),
        "dados_estruturados": {
            "pertinente_ao_banco": analise.pertinente_ao_banco,
            "precisa_clarificacao": False,
            "categoria": analise.categoria,
            "prioridade": analise.prioridade,
            "equipamento": analise.equipamento_afetado,
            "local": analise.local_afetado
        }
    }


@app.get("/api/chamados")
def listar_chamados():
    return ticket_agent.listar_ordens_servico()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
