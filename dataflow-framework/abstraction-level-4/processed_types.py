import typing
from typing import Iterator, Callable, Protocol, Any, Dict, Optional
from pathlib import Path

# A simple transform: str->str
SimpleFn = Callable[[str], str]

# A stream processor: takes an iterator of lines and yields lines
typing.StreamProcessor = Callable[[Iterator[str]], Iterator[str]]

ProcessorConfig = Dict[str, Any]

class StreamProcessor:
    """Base class for stateful stream processors."""
    def __init__(self, config: Optional[ProcessorConfig] = None):
        self.config = config or {}

    def process(self, lines: Iterator[str]) -> Iterator[str]:
        """
        Processes an iterator of lines and yields processed lines.
        Must be implemented by subclasses. This is the core processing logic.
        """
        raise NotImplementedError("Subclasses must implement process()")