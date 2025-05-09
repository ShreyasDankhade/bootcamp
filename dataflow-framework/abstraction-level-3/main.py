
from pathlib import Path
from typing import Iterator, Optional, List
from core import process_lines
from pipeline import load_pipeline
from typess import ProcessorFn

def read_lines(path: Path) -> Iterator[str]:
    """Reads txt file"""
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')


def run(
    input_path: Path,
    output_path: Optional[Path],
    config_path: Path,
) -> None:
    processors: List[ProcessorFn] = load_pipeline(config_path)
    lines = read_lines(input_path)
    transformed = process_lines(lines, processors)

    if output_path:
        with output_path.open('w', encoding='utf-8') as f:
            for line in transformed:
                f.write(line + '\n')
    else:
        for line in transformed:
            print(line)

if __name__ == '__main__':
    from cli import app
    app()