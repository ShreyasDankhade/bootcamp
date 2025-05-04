import typer
from rich import print

app = typer.Typer(help="A small greeting CLI powered by Typer & Rich")

@app.command()
def greet(name: str = typer.Option("world", "-n", "--name", help="Who to say hello to")):
    """
    Print a friendly, styled greeting.
    """
    print(f"[bold magenta]👋 Hello,[/bold magenta] [bold green]{name}[/bold green]!")
