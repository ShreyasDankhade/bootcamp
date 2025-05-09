from typing import Iterator
from processor_types import TaggedLine

def archive_error(lines: Iterator[TaggedLine]) -> Iterator[TaggedLine]:
    """
    Archive error lines; sink node. Yields same (route, line).
    """
    for tag, line in lines:
        # Archive logic goes here
        yield tag, line