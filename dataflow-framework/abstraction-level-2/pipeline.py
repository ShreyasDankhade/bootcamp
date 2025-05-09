from typing import List
from core import to_uppercase, to_snakecase
from typess import ProcessorFn

# Assemble a static pipeline based on the mode

def get_pipeline(mode: str) -> List[ProcessorFn]:
    if mode == 'uppercase':
        return [to_uppercase]
    elif mode == 'snakecase':
        return [to_snakecase]
    else:
        raise ValueError(f"Unknown mode: {mode}")