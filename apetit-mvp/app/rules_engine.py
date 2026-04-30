def filter_menu(menu, profile):
    """
    Filtra o cardápio considerando restrições, objetivo e condição clínica
    """
    filtered = []

    for item in menu:
        # Remove restrições alimentares
        if any(r in item["tags"] for r in profile["restricoes"]):
            continue

        # Regra especial para diabetes
        if "diabetes" in profile.get("condicoes", []):
            if "alto_indice_glicemico" in item["tags"]:
                continue

        # Prioriza objetivo
        if profile["objetivo"] in item["tags"]:
            filtered.append(item)

    return filtered