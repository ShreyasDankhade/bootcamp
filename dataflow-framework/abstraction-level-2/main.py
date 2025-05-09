from pathlib import Path
from typing import Iterator, Optional, List
from core import process_lines
from typess import ProcessorFn

# Read text (including whitespace) from a file
def read_lines(path: Path) -> Iterator[str]:
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')

# Run the processing pipeline and output results

def run(
    input_path: Path,
    output_path: Optional[Path],
    processors: List[ProcessorFn],
) -> None:
    lines = read_lines(input_path)
    transformed = process_lines(lines, processors)

    if output_path:
        with output_path.open('w', encoding='utf-8') as f:
            for line in transformed:
                f.write(line + '\n')
    else:
        for line in transformed:
            print(line)