import typer
from pathlib import Path
from typing import Optional
from main import run

app = typer.Typer()

@app.command()
def main(
    input: Path = typer.Option(..., exists=True, help="Input file path"),
    config: Path = typer.Option(..., exists=True, help="Pipeline YAML file"),
    output: Optional[Path] = typer.Option(None, help="Output file path; stdout if omitted"),
) -> None:
    """
    Run DAG pipeline over input lines.
    """
    run(input, config, output)

