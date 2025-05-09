from typing import Iterator

class LineCounter:
    """
    Stateful processor that prefixes each line with its line number.
    """
    def __init__(self, prefix: str = ''):
        self.count = 0
        self.prefix = prefix

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            self.count += 1
            yield f"{self.prefix}{self.count}: {line}"