import sqlite3
import httpx
from models import AvaliacaoDialogueAgent
from utils import (
    extrair_json_resiliente,
    normalizar_categoria,
    normalizar_prioridade,
    extrair_equipamento_inteligente,
    extrair_local_inteligente,
    resolver_modelo_disponivel
)

class DialogueControlAgent:
    def __init__(self, base_url: str, default_model: str):
        self.base_url = base_url
        self.default_model = default_model

    async def avaliar_dialogo(self, historico: str, mensagem: str) -> AvaliacaoDialogueAgent:
        """
        system_prompt = (
            "# You are a Dialogue Control Agent that manages user questions about an ERP database for company operations.\n\n"
            "# Glossário e Sinônimos Operacionais da Empresa (ADMS / Gestão de Campo):\n"
            "- 'AL' ou 'Alimentador' (ex: AL-03, AL-NORTE): Linha de média tensão de distribuição.\n"
            "- 'DJ' ou 'Disjuntor': Equipamento de manobra e proteção automática da subestação.\n"
            "- 'Trafo', 'TR' ou 'Transformador' (ex: TR-02): Ativo de transformação de tensão.\n"
            "- 'Chave Faca' ou 'Chave Tandem': Mapear para equipamento 'Seccionadora Monopolar'.\n"
            "- '50/51': Atuação por sobrecorrente de fase/neutro (Manutenção Elétrica de Alta Prioridade).\n"
            "- '86': Relé de bloqueio (exige inspeção presencial antes de reenergizar).\n"
            "- 'Padrão P-3' ou 'Padrão P-13': Mapear como infraestrutura de medição de entrada de consumidor.\n\n"
            "# Rules:\n"
            "1. First, verify if the question is about the database (equipment, service orders, electrical maintenance, logistics, billing).\n"
            "2. If it is, decide if the question needs to be rewritten.\n"
            "   - If yes (e.g., user says 'it', 'there', or adds partial info), enrich the question with data from dialogue history.\n"
            "   - Otherwise, use the original question.\n"
            "3. If critical information is missing to register or query the database (e.g. equipment tag or substation), "
            "set precisa_clarificacao = true and formulate a polite clarification question.\n"
            "4. Detect the tom_urgencia_detectado ('CALMO', 'TENSO' or 'PANICO').\n"
            "5. ATTENTION: Do NOT try to convert the question to SQL. Your responsibility is dialogue control and question preparation.\n\n"
            "Respond ONLY a valid JSON object matching this schema:\n"
            "{\n"
            '   "pertinente_ao_banco": true | false,\n'
            '   "precisa_reescrever": true | false,\n'
            '   "pergunta_reescrita": "pergunta enriquecida ou null",\n'
            '   "precisa_clarificacao": true | false,\n'
            '   "pergunta_clarificacao": "pergunta educada ao técnico ou null",\n'
            '   "categoria": "MANUTENCAO_ELETRICA" | "LOGISTICA" | "FATURAMENTO" | "OUTRO",\n'
            '   "prioridade": "BAIXA" | "MEDIA" | "ALTA" | "CRITICA",\n'
            '   "equipamento_afetado": "nome/tag ou NENHUM",\n'
            '   "subestacao_local": "local ou NAO_INFORMADO",\n'
            '   "descricao_resumida": "resumo claro em até 120 caracteres",\n'
            '   "tom_urgencia_detectado": "CALMO" | "TENSO" | "PANICO"\n'
            "}"
        )
        """
        system_prompt = (
            "# ROLE AND CONTEXT\n"
            "You are the senior Autonomous Dialogue Control Agent for an electric power generation and distribution utility company (Empresa de Energia - ADMS/SCADA & Field Operations).\n"
            "Your job is to triage technicians' and field operators' inputs, handle conversation state, extract electrical asset entities, validate missing information (Slot Filling), and prepare sanitized data for the ERP/Database tool.\n\n"
            
            "# ELECTRIC UTILITY GLOSSARY & DOMAIN SYNONYMS (ADMS / Gestão de Campo):\n"
            "- 'Trafo', 'TR' ou 'Transformador' (ex: TR-02, T30): Ativo de transformação de tensão (Subestação ou Distribuição MT/BT).\n"
            "- 'DJ' ou 'Disjuntor': Equipamento de proteção e manobra automática.\n"
            "- 'AL' ou 'Alimentador' (ex: AL-03, AL-NORTE): Circuito/linha de média tensão de distribuição.\n"
            "- 'Chave', 'Chave Faca', 'Chave Seccionadora', 'Chave Tandem': Dispositivo de manobra manual ou telecommandado da rede elétrica.\n"
            "- 'Banco de Capacitores': Ativo de correção de fator de potência na rede.\n"
            "- 'TC' / 'TP': Transformadores de instrumentos (Corrente / Potencial).\n"
            "- '50/51' ou 'Sobrecorrente': Atuação de proteção de fase/neutro (Manutenção Elétrica de Alta Prioridade).\n"
            "- '86' ou 'Relé de Bloqueio': Atuação severa (exige inspeção presencial obrigatória antes de reenergizar).\n"
            "- 'Estrutura', 'Poste', 'Cruzeta', 'Isolador': Elementos físicos da rede de distribuição aérea.\n"
            "- 'Padrão P-3' / 'Padrão P-13': Infraestrutura de medição e entrada do consumidor.\n"
            "- 'BO' / 'Bate-óleo' ou 'Vazamento de óleo': Ocorrência ambiental/elétrica crítica em transformadores.\n\n"
            
            "# OPERATIONAL POLICIES & SAFETY RULES:\n"
            "1. **Relevance Check (pertinente_ao_banco):** Evaluate if the user's message relates to utility operations, electrical maintenance, substations, logistics/freight of equipment, or billing/metering. If it's casual chat or unrelated, set to `false`.\n"
            "2. **Contextual Resolution (precisa_reescrever):** If the message uses pronouns ('it', 'there', 'that transformer') or depends on dialogue history, enrich the question with historical context.\n"
            "3. **Slot Filling & Clarification (precisa_clarificacao):** \n"
            "   - To open a Service Order (OS) for electrical maintenance, the system needs an **Equipment** AND a **Location/Substation**.\n"
            "   - If either is missing (e.g., user says 'the key is broken' without saying where), set `precisa_clarificacao = true` and ask a polite, specific clarification question.\n"
            "   - If the user provided ANY valid equipment (even generic like 'chave' or specific like 'T30') AND a location (like 'Subestação Ahu' or 'Batel'), do NOT ask for clarification; proceed to register.\n"
            "4. **Emotional Tone & Urgency (tom_urgencia_detectado):** Detect the operator's stress level ('CALMO', 'TENSO', or 'PANICO' for cases involving fire, smoke, explosion, sparks, or human risk).\n"
            "5. **Strict Constraint:** Do NOT write SQL queries. Your sole output must be the evaluation JSON matching the schema below.\n\n"
            
            "# JSON SCHEMA:\n"
            "Respond ONLY with a valid JSON object matching this exact structure, with no markdown code blocks wrapping it if possible, or standard clean JSON:\n"
            "{\n"
            '   "pertinente_ao_banco": true,\n'
            '   "precisa_reescrever": false,\n'
            '   "pergunta_reescrita": null,\n'
            '   "precisa_clarificacao": false,\n'
            '   "pergunta_clarificacao": null,\n'
            '   "categoria": "MANUTENCAO_ELETRICA",\n'
            '   "prioridade": "ALTA",\n'
            '   "equipamento_afetado": "Chave Seccionadora",\n'
            '   "subestacao_local": "Subestação Ahu",\n'
            '   "descricao_resumida": "Relato de falha na chave seccionadora",\n'
            '   "tom_urgencia_detectado": "CALMO"\n'
            "}"
        )

        user_content = (
            f"Histórico do Diálogo:\n{historico}\n\n"
            f"Mensagem atual do usuário: \"{mensagem}\"\n\nJSON:"
        )

        modelo_ativo = await resolver_modelo_disponivel(self.base_url, self.default_model)

        payload = {
            "model": modelo_ativo,
            "prompt": f"{system_prompt}\n\n{user_content}",
            "format": "json",
            "stream": False
        }

        try:
            async with httpx.AsyncClient(timeout=25.0) as client:
                res = await client.post(f"{self.base_url}/api/generate", json=payload)
                if res.status_code == 200:
                    corpo = res.json().get("response", "{}")
                    dados = extrair_json_resiliente(corpo)
                    
                    contexto_geral = f"{historico} {mensagem}"
                    cat = normalizar_categoria(dados.get("categoria"), contexto_geral)
                    prio = normalizar_prioridade(dados.get("prioridade"))
                    
                    # Aplicação dos extratores inteligentes com regex
                    equip = extrair_equipamento_inteligente(contexto_geral, str(dados.get("equipamento_afetado", "")))
                    local = extrair_local_inteligente(contexto_geral, str(dados.get("subestacao_local", "")))

                    tom = str(dados.get("tom_urgencia_detectado", "CALMO")).upper()
                    if tom == "PANICO":
                        prio = "CRITICA"

                    desc = str(dados.get("descricao_resumida", mensagem))[:120]
                    pertinente = bool(dados.get("pertinente_ao_banco", True))
                    clarifica = bool(dados.get("precisa_clarificacao", False))
                    pergunta = dados.get("pergunta_clarificacao")
                    reescrita = dados.get("pergunta_reescrita")

                    if cat == "MANUTENCAO_ELETRICA" and (equip in ["NENHUM", ""] or local in ["NAO_INFORMADO", ""]):
                        clarifica = True
                        if not pergunta:
                            pergunta = "Identifiquei uma ocorrência técnica de manutenção elétrica. Poderia informar o equipamento específico e a subestação/local para abrirmos a OS?"

                    return AvaliacaoDialogueAgent(
                        pertinente_ao_banco=pertinente,
                        precisa_reescrever=bool(dados.get("precisa_reescrever", False)),
                        pergunta_reescrita=reescrita,
                        precisa_clarificacao=clarifica,
                        pergunta_clarificacao=pergunta,
                        categoria=cat,
                        prioridade=prio,
                        equipamento_afetado=equip,
                        subestacao_local=local,
                        descricao_resumida=desc,
                        tom_urgencia_detectado=tom if tom in ["CALMO", "TENSO", "PANICO"] else "CALMO"
                    )
        except Exception:
            pass

        # Fallback defensivo determinístico
        t_low = f"{historico} {mensagem}".lower()
        cat = normalizar_categoria(None, t_low)
        prio = "CRITICA" if any(w in t_low for w in ["fumaça", "fogo", "curto", "urgente", "socorro"]) else "ALTA"
        
        equip = extrair_equipamento_inteligente(t_low, "NENHUM")
        local = extrair_local_inteligente(t_low, "NAO_INFORMADO")
        precisa_clarificar = (equip == "NENHUM" or local == "NAO_INFORMADO")

        return AvaliacaoDialogueAgent(
            pertinente_ao_banco=True,
            precisa_reescrever=False,
            pergunta_reescrita=None,
            precisa_clarificacao=precisa_clarificar,
            pergunta_clarificacao="Poderia informar qual o equipamento específico e a subestação/local da ocorrência?" if precisa_clarificar else None,
            categoria=cat,
            prioridade=prio,
            equipamento_afetado=equip,
            subestacao_local=local,
            descricao_resumida=mensagem[:120],
            tom_urgencia_detectado="PANICO" if prio == "CRITICA" else "CALMO"
        )

class TextToSqlAgent:
    @staticmethod
    def compilar_e_executar_insert(cliente_id: int, dados: AvaliacaoDialogueAgent) -> int:
        conn = sqlite3.connect("erp_simulado.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ordens_servico (
                cliente_id, categoria, prioridade, equipamento, subestacao_local, descricao_resumida
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            cliente_id,
            dados.categoria,
            dados.prioridade,
            dados.equipamento_afetado,
            dados.subestacao_local,
            dados.descricao_resumida
        ))
        os_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return os_id