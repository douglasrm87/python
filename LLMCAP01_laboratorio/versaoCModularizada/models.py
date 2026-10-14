from typing import Literal, Optional
from pydantic import BaseModel, Field

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