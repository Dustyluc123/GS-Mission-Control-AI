"""Motor de análise da Mission Control AI - Integração Ollama Cloud."""
import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path
import src.telemetria as telemetria
import src.alertas as alertas

load_dotenv()

TRILHA = "envirosat"
MODELO_LLM = "gpt-oss:120b"

client = Client(
    host="https://ollama.com",
    headers={'Authorization': f'Bearer {os.environ.get("OLLAMA_API_KEY", "")}'}
)

def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    try:
        response = client.chat(
            model=MODELO_LLM,
            messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"⚠ Erro ao consultar a IA via Ollama Cloud: {e}"

def load_system_prompt():
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Tu és um assistente de controlo de missão espacial."

class MissionEngine:
    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()
        
    def is_ready(self):
        return True

    def status_snapshot(self):
        """Retorna o sumário atual da telemetria para o comando /status."""
        dados = telemetria.coletar()
        ultimo = dados[-1]
        return (
            f"=== TELEMETRIA ATUAL (CÁPSULA HELIOS) ===\n"
            f"• Módulo Térmico: {ultimo[0]}°C\n"
            f"• Potência de Sinal: {ultimo[1]}%\n"
            f"• Estado da Bateria (SoC): {ultimo[2]}%\n"
            f"• Oxigénio Base: {ultimo[3]}%\n"
            f"• Alinhamento Dinâmico: {ultimo[4]}%\n"
        )

    def analyze(self, pergunta_usuario):
        """Coleta dados, avalia thresholds e injeta dinamicamente no LLM."""
        dados = telemetria.coletar()
        alertas_gerados = alertas.avaliar(dados)
        
        # Cálculo conceitual do ISE para manter o seu diferencial de Energia
        total_ciclos = len(dados)
        ciclos_ok = sum(1 for c in dados if (c[2] * 1.2 - 65.0) >= 0)
        ise_final = (ciclos_ok / total_ciclos) * 100

        prompt_completo = f"""
======= TELEMETRIA ATUAL DA MISSÃO HELIOS =======
Dados Brutos de Sensor (Último Ciclo):
- Temperatura Módulo Térmico: {dados[-1][0]}°C
- Potência de Sinal/Comunicação: {dados[-1][1]}%
- Estado de Carga da Bateria (SoC): {dados[-1][2]}%
- Suporte de Oxigénio: {dados[-1][3]}%
- Estabilidade de Atitude: {dados[-1][4]}%

Análise Algorítmica (Python):
- Índice de Sustentabilidade Energética (ISE): {ise_final:.1f}%
- Alertas de Subordinação Lógica detetados: {alertas_gerados}

======= SOLICITAÇÃO DO OPERADOR TERRESTRE =======
Pergunta: {pergunta_usuario}

Com base nestes dados orbitais exatos e nas regras do teu System Prompt, emite o teu parecer técnico:
"""
        return llm(prompt_completo, system=self.system_prompt)