"""Motor de análise da Mission Control AI - Integração Ollama Cloud."""
import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Configuração da Trilha e da API (Exigência do Edital de IA)
TRILHA = "envirosat"
MODELO_LLM = "gpt-oss:120b"

# Inicialização do Cliente Oficial Ollama Cloud
client = Client(
    host="https://ollama.com",
    headers={'Authorization': f'Bearer {os.environ.get("OLLAMA_API_KEY", "")}'}
)

def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    """Envia o prompt combinado ao gpt-oss:120b via Ollama Cloud API."""
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
    """Carrega o contexto rico do system_prompt.md."""
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Tu és um assistente de controlo de missão espacial."

class MissionEngine:
    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()
        
    def is_ready(self):
        """Sinaliza à UI que o motor de IA está totalmente implementado."""
        return True

    def analyze(self, pergunta_usuario, dados_missao, metricas_energia, alertas_gerados):
        """
        Injeção Dinâmica de Contexto: Junta dados algorítmicos (Python) 
        com a inteligência contextual (IA Generativa).
        """
        # Construção do Prompt de Contexto Rico (Anti-IA Decorativa)
        prompt_completo = f"""
======= TELEMETRIA ATUAL DA MISSÃO HELIOS =======
Dados Brutos de Sensor (Último Ciclo):
- Temperatura Módulo Térmico: {dados_missao[-1][0]}°C
- Potência de Sinal/Comunicação: {dados_missao[-1][1]}%
- Estado de Carga da Bateria (SoC): {dados_missao[-1][2]}%
- Suporte de Oxigénio: {dados_missao[-1][3]}%
- Estabilidade de Atitude: {dados_missao[-1][4]}%

Análise de Engenharia (Python):
- Índice de Sustentabilidade Energética (ISE): {metricas_energia:.1f}%
- Alertas de Subordinação Lógica detetados: {alertas_gerados}

======= SOLICITAÇÃO DO OPERADOR TERRESTRE =======
Pergunta: {pergunta_usuario}

Com base nestes dados orbitais exatos e nas regras do teu System Prompt, emite o teu parecer técnico:
"""
        # Executa a chamada real ao modelo gpt-oss:120b
        return llm(prompt_completo, system=self.system_prompt)