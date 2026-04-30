from fastapi import FastAPI, Request
import json

from app.classifier import IntentClassifier
from app.rules_engine import load_menu, filter_menu
from app.dialogue import continue_dialog, STATE_START

app = FastAPI()

# IA de classificação
classifier = IntentClassifier()

# Dados fake (MVP)
with open("data/profiles.json", encoding="utf-8") as f:
    PROFILES = json.load(f)

MENU = load_menu()

# Estado simples em memória (MVP)
USER_STATE = {}


@app.post("/webhook")
async def telegram_webhook(request: Request):
    payload = await request.json()

    chat_id = str(payload["message"]["chat"]["id"])
    user_text = payload["message"].get("text", "").lower()
    user_name = payload["message"]["chat"].get("first_name", "Cliente")

    # Estado atual
    state = USER_STATE.get(chat_id, STATE_START)

    # Perfil fixo (MVP)
    profile = PROFILES.get(chat_id, list(PROFILES.values())[0])

    # Classificação por IA
    intent = classifier.classify(user_text)

    # Regras nutricionais
    suggestions = filter_menu(MENU, profile)

    # Diálogo contínuo
    response = continue_dialog(
        intent=intent,
        state=state,
        suggestions=suggestions,
        user_name=user_name
    )

    # Atualiza estado (simples)
    if intent == "despedida":
        USER_STATE[chat_id] = STATE_START
    else:
        USER_STATE[chat_id] = intent

    # Retorno para Telegram API
    return {
        "method": "sendMessage",
        "chat_id": chat_id,
        "text": response["text"],
        "reply_markup": response.get("reply_markup")
    }