"""Motor de análise avançado com Memória Temporal e Múltiplas Personas."""
import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path
import src.telemetria as telemetria
import src.alertas as alertas

load_dotenv()

TRILHA = "envirosat"
MODELO_LLM = "gpt-oss:120b"

# EVITA CRIAR CABEÇALHO INVÁLIDO CASO A CHAVE ESTEJA VAZIA
api_key = os.environ.get("OLLAMA_API_KEY", "").strip()
headers = {}
if api_key:
    headers['Authorization'] = f'Bearer {api_key}'

client = Client(
    host="https://ollama.com",
    headers=headers
)

def llm(prompt, system=None, max_tokens=900, temperature=0.4):
    # TRAVA DE SEGURANÇA CONTEXTUAL: Valida se a chave existe antes de chamar a API
    if not os.environ.get("OLLAMA_API_KEY", "").strip():
        return (
            "❌ [ASTRONAUTA, CHAVE DE API NÃO DETECTADA!]\n\n"
            "O sistema não conseguiu ler a variável 'OLLAMA_API_KEY' no ambiente local.\n\n"
            "COMO RESOLVER:\n"
            "1. Garanta que existe um arquivo com o nome exato '.env' na raiz do projeto.\n"
            "2. Coloque o seu token dentro dele sem aspas, dessa forma:\n"
            "   OLLAMA_API_KEY=seu_token_oficial_fornecido_pelo_professor\n\n"
            "💡 [DICA PARA O VÍDEO]: Caso queira gravar a demonstração sem conectar à API real,\n"
            "você pode adicionar uma chave fictícia no seu .env (ex: OLLAMA_API_KEY=simulado) e\n"
            "fazer a função retornar uma resposta fixa de teste."
        )

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
    return path.read_text(encoding="utf-8") if path.exists() else "Você é um assistente orbital."

class MissionEngine:
    def __init__(self):
        self.trilha = TRILHA
        self.base_system_prompt = load_system_prompt()
        self.historico = []
        self.persona_atual = "OPERADOR"
        self.personas_config = {
            "OPERADOR": "Foque em logs de engenharia brutas, telemetria direta, segurança de hardware e ações imediatas na microrrede.",
            "ASTRONAUTA": "Adote um tom de sobrevivência humana. Foque nos sistemas de suporte à vida (Oxigênio/Temperatura interna) e dê instruções de reparo manuais e simplificadas.",
            "CIENTISTA": "Foque no impacto ecológico na Terra. Relacione os dados de energia com o monitoramento do INPE/IBAMA contra o desmatamento na Amazonia."
        }

    def is_ready(self):
        return True

    def trocar_persona(self, nova_persona):
        nova_persona = nova_persona.upper()
        if nova_persona in self.personas_config:
            self.persona_atual = nova_persona
            return f"🔄 Persona alterada com sucesso! Perfil ativo: [bold #06B6D4]{nova_persona}[/bold #06B6D4]."
        return f"❌ Persona inválida. Escolha entre: {', '.join(self.personas_config.keys())}"

    def status_snapshot(self):
        if not self.historico:
            self.historico.append(telemetria.coletar())
        ultimo = self.historico[-1]
        return (
            f"=== SNAPSHOT DE TELEMETRIA (PERFIL: {self.persona_atual}) ===\n"
            f"• Módulo Térmico: {ultimo[0]}°C\n"
            f"• Potência de Sinal: {ultimo[1]}%\n"
            f"• Estado da Bateria (SoC): {ultimo[2]}%\n"
            f"• Oxigênio Base: {ultimo[3]}%\n"
            f"• Alinhamento Dinâmico: {ultimo[4]}%\n"
            f"• Ciclos Armazenados na Memória Temporal: {len(self.historico)}"
        )

    def analyze(self, pergunta_usuario):
        novo_ciclo = telemetria.coletar()
        self.historico.append(novo_ciclo)
        if len(self.historico) > 5:
            self.historico.pop(0)
            
        alertas_gerados = alertas.avaliar(self.historico)
        
        linha_tempo_str = ""
        for i, ciclo in enumerate(self.historico):
            linha_tempo_str += f" -> Ciclo T-{len(self.historico)-i-1}: Temp={ciclo[0]}°C, Sinal={ciclo[1]}%, Bat={ciclo[2]}%, O2={ciclo[3]}%, Est={ciclo[4]}%\n"

        system_prompt_customizado = f"""
        {self.base_system_prompt}
        
        [DIRETRIZ DE PERSONA ATIVA]
        Você deve responder assumindo estritamente a identidade de um: {self.persona_atual}.
        Instrução específica de atuação: {self.personas_config[self.persona_atual]}
        """

        prompt_completo = f"""
======= HISTÓRICO TEMPORAL DE TELEMETRIA (ÚLTIMOS CICLOS) =======
{linha_tempo_str}
================================================================

VETOR ATUAL ATINGIDO:
- Alertas lógicos gerados pelo script Python: {alertas_gerados}

======= SOLICITAÇÃO DO USUÁRIO =======
Pergunta: {pergunta_usuario}

Com base na linha temporal acima, identifique tendências de piora ou melhora, assuma a sua persona ativa e emita o parecer técnico:
"""
        return llm(prompt_completo, system=system_prompt_customizado)