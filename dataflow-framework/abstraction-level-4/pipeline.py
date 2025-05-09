from core import stream_processor
from processors.stateless import to_uppercase, to_snakecase
from processors.counter import LineCounter
from processors.fan_in import JoinEvery
from processors.fan_out import SplitOn
from typing import List
from processed_types import StreamProcessor


def get_pipeline() -> List[StreamProcessor]:
    # Example static assembly with mixed processors:
    return [
        stream_processor(to_snakecase),  # processing
        JoinEvery(n=2, sep=' || '),      # fan-in every 2 lines
        LineCounter(prefix='Line '),     # stateful counter
        SplitOn(delimiter='-'),          # fan-out on '-'
        stream_processor(to_uppercase),  # process again
    ]