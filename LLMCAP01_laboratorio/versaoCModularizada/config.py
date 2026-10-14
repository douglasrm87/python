import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODELO_LLM_PREFERENCIAL = os.getenv("MODELO_LLM", "llama3.2:1b")