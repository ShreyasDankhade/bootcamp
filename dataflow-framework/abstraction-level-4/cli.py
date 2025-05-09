import typer
from pathlib import Path
from typing import Optional
from main import run

app = typer.Typer()

@app.command()
def main(
    input: Path = typer.Option(..., exists=True, help="Input file path"),
    output: Optional[Path] = typer.Option(None, help="Output file path; stdout if omitted"),
):
    """
    Run the stream-processing pipeline over INPUT.
    Joins every 2 lines as one single line.
    Splits the line on the delimiter (i.e.'-')

    """
    run(input, output)