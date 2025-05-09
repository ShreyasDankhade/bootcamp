from typing import Iterator, List
from typess import ProcessorFn


def process_line(line: str, processors: List[ProcessorFn]) -> str:
    for proc in processors:
        line = proc(line)
    return line


def process_lines(
    lines: Iterator[str],
    processors: List[ProcessorFn]
) -> Iterator[str]:
    for line in lines:
        yield process_line(line, processors)