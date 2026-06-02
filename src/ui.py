"""Interface CLI estilo Claude Code — usa Rich + prompt-toolkit."""
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
        "Sistema de monitorização e análise por IA generativa.\n"
        "Use /help para ver os comandos · /status para ver telemetria · /exit para sair.\n"
        "Modelo: gpt-oss:120b via Ollama Cloud", 
        title="◆ CORE SYSTEMS", border_style="#06B6D4"
    ))

def show_response(text):
    now = datetime.now().strftime("%H:%M")
    console.print(Panel(text, title="◆ Helios Core AI", subtitle=now, border_style="#06B6D4"))

def run_cli(engine):
    show_banner()
    if not engine.is_ready():
        console.print(" ⚠ Engine status: AGUARDANDO IMPLEMENTAÇÃO ✗\n", style="yellow")
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
            console.print("[bold #06B6D4]Comandos disponíveis:[/bold #06B6D4] /help · /status · /clear · /exit")
            continue
        if user_input == "/status":
            show_response(engine.status_snapshot())
            continue
        if user_input == "/clear":
            console.clear()
            show_banner()
            continue

        resposta = engine.analyze(user_input)
        show_response(resposta)