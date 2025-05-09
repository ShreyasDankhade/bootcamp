import os
from pathlib import Path
from typing import Iterator, Optional

import typer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def read_lines(path: Path) -> Iterator[str]:
    """Reads text-file from the given file path."""
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip("\n")


def transform_line(line: str, mode: str) -> str:
    """Transform text based on the selected mode."""
    if mode == "uppercase":
        return line.strip().upper()
    elif mode == "snakecase":
        return line.strip().replace(" ", "_").lower()
    else:
        typer.echo(f"Error: Unsupported mode '{mode}'. Use 'uppercase' or 'snakecase'.")
        raise typer.Exit(code=1)


def write_output(lines: Iterator[str], output_path: Optional[Path]) -> None:
    """Write transformed lines to stdout or to the specified output file."""
    if output_path:
        with output_path.open('w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + "\n")
    else:
        for line in lines:
            typer.echo(line)


app = typer.Typer(help="Process text files with different transformation modes.")


@app.command()
def main(
    input: Path = typer.Option(..., exists=True, readable=True, help="Path to input file"),
    output: Optional[Path] = typer.Option(None, help="Path to output file; defaults to stdout"),
    mode: str = typer.Option(
        os.getenv("MODE", "uppercase"),
        help="Processing mode: 'uppercase' or 'snakecase'",
    ),
):
    """
    Read lines from INPUT, transform each line according to MODE, and write to OUTPUT or stdout.
    """
    lines = (transform_line(line, mode) for line in read_lines(input))
    write_output(lines, output)


if __name__ == "__main__":
    app()
