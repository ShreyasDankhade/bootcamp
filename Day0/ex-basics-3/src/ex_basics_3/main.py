import typer
from rich import print

app = typer.Typer(help="Simple calculator commands")

@app.command()
def add(
    a: float = typer.Argument(..., help="First number"),
    b: float = typer.Argument(..., help="Second number")
):
    """Add two numbers."""
    result = a + b
    print(f"[bold green]{a} + {b} = {result}[/bold green]")

@app.command()
def sub(
    a: float = typer.Argument(..., help="First number"),
    b: float = typer.Argument(..., help="Second number")
):
    """Subtract two numbers."""
    result = a - b
    print(f"[bold green]{a} – {b} = {result}[/bold green]")

@app.command()
def mul(
    a: float = typer.Argument(..., help="First number"),
    b: float = typer.Argument(..., help="Second number")
):
    """Multiply two numbers."""
    result = a * b
    print(f"[bold green]{a} × {b} = {result}[/bold green]")

@app.command()
def div(
    a: float = typer.Argument(..., help="Dividend"),
    b: float = typer.Argument(..., help="Divisor")
):
    """Divide two numbers."""
    if b == 0:
        print("[bold red]Error:[/bold red] Division by zero")
        raise typer.Exit(code=1)
    result = a / b
    print(f"[bold green]{a} ÷ {b} = {result}[/bold green]")

