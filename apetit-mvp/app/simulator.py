"""
simulator.py
Simulador de conversa automática para testes do chatbot APETIT
pip install scikit-learn
"""

import json

from classifier import IntentClassifier
from rules_engine import load_menu, filter_menu
from dialogue import (
    continue_dialog,
    STATE_START
)

# -------------------------------
# Dados do MVP
# -------------------------------

with open("data/profiles.json", encoding="utf-8") as f:
    PROFILES = json.load(f)

MENU = load_menu()

# Usuário simulado
CHAT_ID = "123456"
USER_NAME = "Ana"

PROFILE = PROFILES[CHAT_ID]

# Classificador
classifier = IntentClassifier()

# Estado da conversa
state = STATE_START

# Conversas simuladas
USER_MESSAGES = [
    "Oi",
    "Quero uma recomendação",
    "Gostei",
    "Quero outra sugestão",
    "Ver outras opções",
    "Não gostei",
    "Obrigado",
    "Sou diabética",
    "Quero uma recomendação"

]


def simulate_conversation():
    global state

    print("\n🟢 INÍCIO DA SIMULAÇÃO DE CONVERSA\n")

    for message in USER_MESSAGES:
        print(f"👤 Usuário: {message}")

        # Classificação
        intent = classifier.classify(message)

        # Regras nutricionais
        suggestions = filter_menu(MENU, PROFILE)

        # Diálogo
        response = continue_dialog(
            intent=intent,
            state=state,
            suggestions=suggestions,
            user_name=USER_NAME
        )

        # Exibe resposta
        print(f"🤖 Bot: {response['text']}")

        # Botões simulados
        if "reply_markup" in response:
            buttons = [
                btn[0] for btn in response["reply_markup"]["keyboard"]
            ]
            print(f"🔘 Opções: {buttons}")

        # Atualiza estado
        if intent == "despedida":
            state = STATE_START
        else:
            state = intent

        print("-" * 50)

    print("\n🔴 FIM DA SIMULAÇÃO\n")


if __name__ == "__main__":
    simulate_conversation()