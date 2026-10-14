from typing import Dict, List, Optional
from uuid import uuid4

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