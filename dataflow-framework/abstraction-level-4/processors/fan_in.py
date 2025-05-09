from typing import Iterator, List

class JoinEvery:
    """
    Fan-in processor: joins every N lines into one, separated by a delimiter.
    """

    def __init__(self, n: int = 2, sep: str = ' '):
        self.n = n
        self.sep = sep

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        buffer: List[str] = []
        for line in lines:
            buffer.append(line)
            if len(buffer) >= self.n:
                yield self.sep.join(buffer)
                buffer.clear()
        # emit leftover
        if buffer:
            yield self.sep.join(buffer)