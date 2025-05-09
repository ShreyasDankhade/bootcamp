def to_snakecase(line: str) -> str:
    """Strip whitespace, replace spaces with underscores, convert to lowercase"""
    return line.strip().replace(' ', '_').lower()