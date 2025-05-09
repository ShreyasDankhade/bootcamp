from typing import Callable

# A processor takes a single line and returns the transformed line
ProcessorFn = Callable[[str], str]