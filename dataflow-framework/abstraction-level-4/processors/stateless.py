

def to_uppercase(line: str) -> str:
    return line.strip().upper()


def to_snakecase(line: str) -> str:
    return line.strip().replace(' ', '_').lower()