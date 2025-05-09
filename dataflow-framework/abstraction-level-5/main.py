from pathlib import Path
from typing import Iterator, Tuple, Optional, List
from engine import load_pipeline_config, run_engine, RoutingError
from processor_types import TaggedLine

def read_raw(
    input_path: Path
) -> Iterator[TaggedLine]:
    """
    Read lines, tagging each with 'default'.
    """
    with input_path.open('r', encoding='utf-8') as f:
        for line in f:
            yield 'default', line.rstrip('\n')

def write_grouped(
    lines: Iterator[TaggedLine],
    output_path: Optional[Path]
) -> None:
    """
    Group INFO, warning, and error lines and write in a clean format—
    only one summary per category (using the last summary emitted).
    """
    last_warn_summary: Optional[str] = None
    last_err_summary:  Optional[str] = None
    infos: List[str] = []

    for tag, text in lines:
        if text.startswith('[INFO]'):
            infos.append(text)
        elif tag == 'warning':
            last_warn_summary = text
        elif tag == 'error':
            last_err_summary = text

    out: List[str] = []
    # 1. All INFOs
    out.extend(infos)
    if infos:
        out.append('')  # blank line

    # 2. Single Warnings summary
    if last_warn_summary:
        # The summary text already includes count and messages
        out.append(last_warn_summary)
        out.append('')  # blank line

    # 3. Single Errors summary
    if last_err_summary:
        out.append(last_err_summary)

    content = "\n".join(out)

    if output_path:
        with output_path.open('w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(content)

def run(
    input_path: Path,
    config_path: Path,
    output_path: Optional[Path]
) -> None:
    """
    Load config, execute engine, and write grouped outputs.
    """
    try:
        nodes, routing = load_pipeline_config(config_path)
    except RoutingError as e:
        print(f"Config error: {e}")
        return

    raw = read_raw(input_path)
    processed = run_engine(raw, nodes, routing)
    write_grouped(processed, output_path)

if __name__ == '__main__':
    from cli import app
    app()
