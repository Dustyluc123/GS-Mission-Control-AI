"""Interface CLI avançada com suporte a comandos de mudança de persona."""
from rich.console import Console
from rich.panel import Panel
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from datetime import datetime

console = Console()
session = PromptSession(style=Style.from_dict({"prompt": "#06B6D4 bold"}))

def show_banner():
    console.print(Panel(
        "[bold #06B6D4]MISSION CONTROL AI - HELIOS ENERGY EDITION[/bold #06B6D4]\n"
        "Comandos Básicos:  /status para ver telemetria  ·  /clear para limpar  ·  /exit para sair\n"
        "Múltiplas Personas: Tipo [bold #A855F7]/persona operador[/bold #A855F7] | [bold #A855F7]/persona astronauta[/bold #A855F7] | [bold #A855F7]/persona cientista[/bold #A855F7]\n"
        "Modelo Ativo: gpt-oss:120b com Memória Temporal Ativa (Últimos 5 Ciclos)", 
        title="◆ SYSTEMS OPERATIONAL", border_style="#06B6D4"
    ))

def show_response(text, titulo="◆ Helios Core AI"):
    now = datetime.now().strftime("%H:%M")
    console.print(Panel(text, title=titulo, subtitle=now, border_style="#06B6D4"))

def run_cli(engine):
    show_banner()
    while True:
        try:
            user_input = session.prompt("❯ ").strip()
        except (KeyboardInterrupt, EOFError):
            break
        if not user_input:
            continue
        if user_input == "/exit":
            break
        if user_input == "/help":
            console.print("[bold #06B6D4]Comandos:[/bold #06B6D4] /help · /status · /clear · /persona <tipo> · /exit")
            continue
        if user_input == "/status":
            show_response(engine.status_snapshot(), titulo="◆ Status Snapshot")
            continue
        if user_input == "/clear":
            console.clear()
            show_banner()
            continue
            
        # Tratamento do comando customizado de Múltiplas Personas
        if user_input.startswith("/persona "):
            nova_persona = user_input.replace("/persona ", "").strip()
            resultado = engine.trocar_persona(nova_persona)
            console.print(resultado)
            continue

        # Fluxo de análise normal com IA
        resposta = engine.analyze(user_input)
        show_response(resposta, titulo=f"◆ Resposta ({engine.persona_atual})")