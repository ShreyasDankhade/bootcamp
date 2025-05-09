
import typer
from pathlib import Path
from typing import Optional
from main import run

app = typer.Typer()

@app.command()
def main(
    input: Path = typer.Option(..., exists=True, readable=True, help="Input file path"),
    output: Optional[Path] = typer.Option(None, help="Output file path; stdout if omitted"),
    config: Path = typer.Option(
        Path('pipeline.yaml'),
        exists=True,
        readable=True,
        help="YAML pipeline config file"
    ),
):
    run(input, output, config)

if __name__ == '__main__':
    app()