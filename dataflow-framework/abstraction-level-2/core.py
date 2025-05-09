from typing import Iterator, List
from typess import ProcessorFn

# Processor implementations:
def to_uppercase(line: str) -> str:
    return line.strip().upper()

def to_snakecase(line: str) -> str:
    return line.strip().replace(' ', '_').lower()

# Apply a sequence of processors to one line
def process_line(line: str, processors: List[ProcessorFn]) -> str:
    for proc in processors:
        line = proc(line)
    return line

# Transform an iterator of lines
def process_lines(lines: Iterator[str], processors: List[ProcessorFn]) -> Iterator[str]:
    for line in lines:
        yield process_line(line, processors)