def clean_text(text: str) -> str:
    """Remove unnecessary whitespace from text."""
    return text.strip()


def is_non_empty_text(text: str) -> bool:
    """Check whether text contains meaningful content."""
    return bool(text and text.strip())


def truncate_text(text: str, max_length: int = 1000) -> str:
    """Limit text to a maximum number of characters."""
    return text[:max_length]
