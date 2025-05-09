import importlib
from pathlib import Path
from typing import List
import yaml
from typess import ProcessorFn


def load_pipeline(config_path: Path) -> List[ProcessorFn]:
    """
    Parse the YAML config, dynamically import each processor, and return a list of callables.
    """
    try:
        config_file = yaml.safe_load(config_path.read_text(encoding='utf-8'))
    except Exception as e:
        raise RuntimeError(f"Failed to load config '{config_path}': {e}")

    if 'pipeline' not in config_file or not isinstance(config_file['pipeline'], list):
        raise ValueError("Config file must contain 'pipeline' as a list")

    processors = []
    for entry in config_file['pipeline']:
        if 'type' not in entry:
            raise ValueError(f"Pipeline entry missing 'type': {entry}")
        type_path = entry['type']
        module_path, func_name = type_path.rsplit('.', 1)

        try:
            module = importlib.import_module(module_path)
        except ImportError as e:
            raise ImportError(f"Cannot import module '{module_path}': {e}")

        try:
            func = getattr(module, func_name)
        except AttributeError:
            raise ImportError(f"Module '{module_path}' has no attribute '{func_name}'")

        if not callable(func):
            raise TypeError(f"Processor '{type_path}' is not callable")

        processors.append(func)

    return processors