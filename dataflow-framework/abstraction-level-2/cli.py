import os
from pathlib import Path
from typing import Optional
import typer
from dotenv import load_dotenv
from pipeline import get_pipeline
from main import run

# Load MODE from .env if present
env_file = Path('.env')
if env_file.exists():
    load_dotenv(env_file)

app = typer.Typer()

@app.command()
def main(
    input: Path = typer.Option(..., exists=True, readable=True, help="Path to input file"),
    output: Optional[Path] = typer.Option(None, help="Path to output file (defaults to stdout)"),
    mode: str = typer.Option(
        os.getenv('MODE'),
        help="Processing mode: 'uppercase' or 'snakecase'"
    ),
):
    processors = get_pipeline(mode)
    run(input, output, processors)

if __name__ == '__main__':
    app()