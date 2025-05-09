from typing import Iterator, List
from processor_types import TaggedLine

class WarningTally:
    """
    Stateful processor counting warning lines; emits a summary tagged as 'warning'
    with the messages seen.
    """
    def __init__(self) -> None:
        self.count: int = 0
        self.messages: List[str] = []

    def __call__(self, lines: Iterator[TaggedLine]) -> Iterator[TaggedLine]:
        for tag, text in lines:
            # Only count lines actually tagged as warnings
            if tag == 'warning':
                self.count += 1
                self.messages.append(text)

        summary = f"Warnings ({self.count}):"
        parts = [f" • {msg}" for msg in self.messages]
        yield 'warning', "\n".join([summary] + parts)
