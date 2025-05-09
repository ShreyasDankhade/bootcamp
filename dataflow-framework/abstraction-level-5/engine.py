import importlib
import inspect
from pathlib import Path
from collections import deque
from typing import Dict, Iterator, Tuple
import yaml
from processor_types import TaggedLine, StreamProcessor, Route

class RoutingError(Exception):
    """Raised when routing or config is invalid."""
    pass


def load_pipeline_config(
    config_path: Path
) -> Tuple[Dict[str, StreamProcessor], Dict[str, Dict[Route, str]]]:
    """
    Load YAML pipeline config, import processors, build routing table.
    """
    data = yaml.safe_load(config_path.read_text(encoding='utf-8'))
    nodes = data.get('nodes', {})
    node_map: Dict[str, StreamProcessor] = {}
    routing_map: Dict[str, Dict[Route, str]] = {}

    for name, cfg in nodes.items():
        proc_path = cfg['processor']
        module_name, attr = proc_path.rsplit('.', 1)
        module = importlib.import_module(module_name)
        proc_obj = getattr(module, attr)
        # Instantiate class-based processors
        if inspect.isclass(proc_obj):
            proc = proc_obj()
        else:
            proc = proc_obj
        if not callable(proc):
            raise RoutingError(f"Processor {proc_path} not callable")
        node_map[name] = proc
        routing_map[name] = cfg.get('outputs', {})
    return node_map, routing_map


def run_engine(
    lines: Iterator[TaggedLine],
    node_map: Dict[str, StreamProcessor],
    routing_map: Dict[str, Dict[Route, str]]
) -> Iterator[TaggedLine]:
    """
    Execute lines through the DAG, yielding terminal outputs.
    """
    queue = deque(( 'trim', tl ) for tl in lines)
    while queue:
        node, (route, text) = queue.popleft()
        if node not in node_map:
            raise RoutingError(f"Unknown node: {node}")
        proc = node_map[node]
        outputs = routing_map.get(node, {})
        for out_tag, out_text in proc(iter([(route, text)])):
            next_node = outputs.get(out_tag, outputs.get('default'))
            # Terminate on 'end' or missing node
            if not next_node or next_node == 'end':
                yield out_tag, out_text
            else:
                queue.append((next_node, (out_tag, out_text)))