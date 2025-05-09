from typing import Iterator, Tuple, Callable

# A routing tag
Route = str

# A tagged line: (route, payload)
TaggedLine = Tuple[Route, str]

# A processor over tagged lines
StreamProcessor = Callable[[Iterator[TaggedLine]], Iterator[TaggedLine]]