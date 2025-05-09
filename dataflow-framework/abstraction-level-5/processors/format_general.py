from typing import Iterator
from processor_types import TaggedLine

def format_general(lines: Iterator[TaggedLine]) -> Iterator[TaggedLine]:
    """
    Format general messages for output.
    """
    for tag, line in lines:
        yield 'default', f"[INFO] {line}"