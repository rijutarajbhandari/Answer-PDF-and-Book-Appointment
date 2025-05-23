import re
import dateparser

def is_valid_email(email: str) -> bool:
    """Validate email address format."""
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))


def is_valid_phone(phone: str) -> bool:
    """
    Validate international phone number.
    Accepts digits with optional + and length between 10 and 15.
    """
    return bool(re.match(r"^\+?\d{10,15}$", phone))


def parse_date_from_text(text: str) -> str | None:
    parsed = dateparser.parse(
        text,
        settings={'PREFER_DATES_FROM': 'future'}
    )
    return parsed.strftime("%Y-%m-%d") if parsed else None