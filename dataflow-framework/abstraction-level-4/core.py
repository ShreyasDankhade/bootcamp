from typing import Iterator, List
from processed_types import StreamProcessor, SimpleFn


def stream_processor(fn: SimpleFn) -> StreamProcessor:
    """
        Wraps a simple line‐transforming function so it can
        consume and yield a stream of lines.
    """
    def processor(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield fn(line)
    return processor


def process_stream(
    lines: Iterator[str],
    processors: List[StreamProcessor]
) -> Iterator[str]:
    """Pipe the lines through each stream processor in sequence."""
    for proc in processors:
        lines = proc(lines)
    return lines