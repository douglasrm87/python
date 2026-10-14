import json
import re
import httpx
from typing import Optional

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
    if any(k in t_low for k in ["transformador", "disjuntor", "fumaça", "curto", "subestação", "rede", "óleo", "chave", "alimentador", "trafo", "dj", "al", "t30"]):
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

def extrair_equipamento_inteligente(texto: str, equipamento_llm: str) -> str:
    """Captura o equipamento e sua tag específica (ex: T30, TR-02, AL-03, DJ-01) do texto."""
    t_low = texto.lower()
    match = re.search(r'\b(tr-?\d+|t-?\d+|al-?\d+|dj-?\d+|trafo\s*\w+)\b', t_low)
    if match:
        tag = match.group(1).upper()
        base = "Transformador" if "t" in tag or "tr" in tag else ("Alimentador" if "al" in tag else ("Disjuntor" if "dj" in tag else "Equipamento"))
        return f"{base} {tag}"
    if equipamento_llm and equipamento_llm not in ["NENHUM", ""]:
        return equipamento_llm
    if "trafo" in t_low or "transformador" in t_low:
        return "Transformador"
    if "disjuntor" in t_low or "dj" in t_low:
        return "Disjuntor"
    if "alimentador" in t_low or "al" in t_low:
        return "Alimentador"
    return "NENHUM"

def extrair_local_inteligente(texto: str, local_llm: str) -> str:
    """Captura subestações mencionadas no texto."""
    t_low = texto.lower()
    if "ahu" in t_low:
        return "Subestação Ahu"
    if "batel" in t_low:
        return "Subestação Batel"
    if "norte" in t_low:
        return "Subestação Norte"
    if local_llm and local_llm not in ["NAO_INFORMADO", ""]:
        return local_llm
    return "NAO_INFORMADO"

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