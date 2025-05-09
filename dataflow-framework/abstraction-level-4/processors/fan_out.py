from typing import Iterator

class SplitOn:
    """
    Fan-out processor: splits each line on a delimiter and yields each part.
    """
    def __init__(self, delimiter: str = ','):
        self.delim = delimiter

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            for part in line.split(self.delim):
                yield part.strip()