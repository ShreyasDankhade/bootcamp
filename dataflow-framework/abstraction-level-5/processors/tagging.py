from typing import Iterator
from processor_types import TaggedLine

def tag_error_warn(lines: Iterator[TaggedLine]) -> Iterator[TaggedLine]:
    """
    Tag lines containing 'ERROR' or 'WARN', default otherwise.
    """
    for _, line in lines:
        text = line.strip()
        if 'ERROR' in text:
            tag = 'error'
        elif 'WARN' in text:
            tag = 'warning'
        else:
            tag = 'default'
        yield tag, text