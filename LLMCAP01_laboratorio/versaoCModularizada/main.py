import os
import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from config import OLLAMA_BASE_URL, MODELO_LLM_PREFERENCIAL
from database import init_erp_db
from models import MensagemChatRequest, RespostaChat
from memory import memoria_global
from agents import DialogueControlAgent, TextToSqlAgent

init_erp_db()

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

dialogue_control = DialogueControlAgent(OLLAMA_BASE_URL, MODELO_LLM_PREFERENCIAL)
sql_tool = TextToSqlAgent()

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

@app.get("/chamados", include_in_schema=False)
async def chamados_view_route():
    if os.path.exists("chamados.html"):
        return FileResponse("chamados.html")
    return {"status": "ok", "mensagem": "Arquivo chamados.html não localizado na pasta raiz."}

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