from typing import Iterator
from processor_types import TaggedLine

def trim(lines: Iterator[TaggedLine]) -> Iterator[TaggedLine]:
    """
    Strip leading/trailing whitespace, collapse internal whitespace sequences,
    and preserve routing tag.
    """
    for route, line in lines:
        # Remove leading/trailing whitespace
        stripped = line.strip()
        # Collapse multiple internal whitespace into a single space
        normalized = " ".join(stripped.split())
        yield route, normalized
