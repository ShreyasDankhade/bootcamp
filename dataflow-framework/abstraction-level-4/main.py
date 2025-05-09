from pathlib import Path
from typing import Iterator, Optional, List
from core import process_stream
from pipeline import get_pipeline
from processed_types import StreamProcessor



def read_lines(path: Path) -> Iterator[str]:
    """
    Read lines from the input.txt provided.
    """
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')


def write_lines(lines: Iterator[str], output: Optional[Path]) -> None:
    """
    Returns the file user needs
    """
    if output:
        with output.open('w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
    else:
        for line in lines:
            print(line)


def run(input_path: Path, output_path: Optional[Path]) -> None:
    # Build pipeline
    processors: List[StreamProcessor] = get_pipeline()

    # Read, process, write
    lines = read_lines(input_path)
    processed = process_stream(lines, processors)
    write_lines(processed, output_path)


if __name__ == '__main__':
    from cli import app
    app()
