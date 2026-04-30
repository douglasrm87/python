"""
dialogue.py
Responsável por gerenciar o diálogo contínuo do chatbot nutricional (MVP APETIT)
"""

from typing import List, Dict, Optional

# ------------------------------
# Estados possíveis do diálogo
# ------------------------------
STATE_START = "inicio"
STATE_RECOMMENDATION = "recomendacao"
STATE_FEEDBACK = "feedback"
STATE_OTHER_OPTIONS = "outras_opcoes"
STATE_END = "fim"


def build_response(
    text: str,
    buttons: Optional[List[str]] = None
) -> Dict:
    """
    Monta a resposta padrão para o Telegram
    """
    response = {"text": text}

    if buttons:
        response["reply_markup"] = {
            "keyboard": [[btn] for btn in buttons],
            "resize_keyboard": True,
            "one_time_keyboard": True
        }

    return response


def start_dialog(user_name: str) -> Dict:
    """
    Início do diálogo
    """
    return build_response(
        text=(
            f"Olá, {user_name}! 👋\n\n"
            "Sou o assistente nutricional do restaurante 🍽️\n"
            "Posso te ajudar com sugestões de pratos de acordo com seu perfil."
        ),
        buttons=[
            "Quero uma recomendação",
            "Ver cardápio do dia"
        ]
    )


def recommend_dish(suggestions: List[Dict]) -> Dict:
    """
    Primeira recomendação baseada no perfil
    """
    if not suggestions:
        return build_response(
            text=(
                "No momento não encontrei pratos ideais para o seu perfil 😕\n"
                "Deseja falar com um atendente?"
            ),
            buttons=["Sim", "Não"]
        )

    first = suggestions[0]["name"]

    return build_response(
        text=(
            f"Com base no seu perfil, recomendo:\n\n"
            f"🥗 *{first}*\n\n"
            "O que você acha?"
        ),
        buttons=[
            "Gostei",
            "Ver outras opções",
            "Não gostei"
        ]
    )


def show_other_options(suggestions: List[Dict]) -> Dict:
    """
    Exibe outras opções do cardápio compatíveis
    """
    if len(suggestions) <= 1:
        return build_response(
            text="Não há outras opções no momento 😕",
            buttons=["Encerrar"]
        )

    options_text = "\n".join(
        [f"• {item['name']}" for item in suggestions[1:]]
    )

    return build_response(
        text=(
            "Aqui estão outras opções adequadas ao seu perfil:\n\n"
            f"{options_text}\n\n"
            "Deseja escolher alguma delas?"
        ),
        buttons=["Gostei", "Encerrar"]
    )


def handle_feedback(feedback_type: str) -> Dict:
    """
    Trata o feedback do usuário
    """
    if feedback_type == "positivo":
        return build_response(
            text=(
                "Que ótimo! 😊\n"
                "Ficamos felizes em ajudar na sua escolha.\n\n"
                "Deseja algo mais?"
            ),
            buttons=["Nova recomendação", "Encerrar"]
        )

    if feedback_type == "negativo":
        return build_response(
            text=(
                "Entendo 👍\n"
                "Posso tentar melhorar a recomendação."
            ),
            buttons=["Ver outras opções", "Encerrar"]
        )

    return build_response(text="Obrigado pelo seu feedback! 😊")


def continue_dialog(
    intent: str,
    state: str,
    suggestions: List[Dict],
    user_name: str = "Cliente"
) -> Dict:
    """
    Controlador principal do diálogo contínuo
    """

    # Início
    if state == STATE_START:
        return start_dialog(user_name)

    # Intenção: recomendação
    if intent == "recomendacao" and state != STATE_FEEDBACK:
        return recommend_dish(suggestions)

    # Usuário pediu outras opções
    if intent == "outras_opcoes":
        return show_other_options(suggestions)

    # Feedback positivo
    if intent == "feedback_positivo":
        return handle_feedback("positivo")

    # Feedback negativo
    if intent == "feedback_negativo":
        return handle_feedback("negativo")

    # Encerramento
    if intent == "despedida":
        return build_response(
            text=(
                "Obrigado pela visita! 👋\n"
                "Sempre que precisar de sugestões nutricionais, estarei por aqui."
            )
        )

    # Fallback
    return build_response(
        text=(
            "Desculpa, não entendi muito bem 😅\n"
            "Posso te ajudar com uma recomendação de prato?"
        ),
        buttons=["Quero uma recomendação", "Encerrar"]
    )