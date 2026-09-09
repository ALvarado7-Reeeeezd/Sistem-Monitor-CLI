import time
import psutil
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

console = Console()

def generate_stats():
    table = Table(title="System Monitor Minimalis", expand=True)
    table.add_column("Komponen", style="cyan", no_wrap=True)
    table.add_column("Penggunaan", style="magenta")

    # Ambil data CPU dan RAM
    cpu_usage = psutil.cpu_percent(interval=None)
    ram_usage = psutil.virtual_memory().percent

    table.add_row("CPU Usage", f"{cpu_usage}%")
    table.add_row("RAM Usage", f"{ram_usage}%")

    return Panel(table, title="[bold green]CLI Dashboard[/bold green]", border_style="blue")

# Loop buat auto-refresh tiap 1 detik
with Live(generate_stats(), refresh_per_second=1) as live:
    try:
        while True:
            time.sleep(1)
            live.update(generate_stats())
    except KeyboardInterrupt:
        console.print("\n[bold red]Monitor dihentikan![/bold red]")