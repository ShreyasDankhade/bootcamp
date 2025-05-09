from typing import Iterator, List
from processor_types import TaggedLine

class ErrorTally:
    """
    Stateful processor counting error lines; emits a summary tagged as 'error'
    with the messages seen.
    """
    def __init__(self) -> None:
        self.count: int = 0
        self.messages: List[str] = []

    def __call__(self, lines: Iterator[TaggedLine]) -> Iterator[TaggedLine]:
        for tag, text in lines:
            if tag == 'error':
                self.count += 1
                self.messages.append(text)

        summary = f"Errors ({self.count}):"
        parts = [f" • {msg}" for msg in self.messages]
        yield 'error', "\n".join([summary] + parts)
