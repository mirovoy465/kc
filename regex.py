import re
from typing import List

VALID_EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")

def valid_emails(strings: List[str]) -> List[str]:
    """Take list of potential emails and returns only valid ones"""

    def is_valid_email(email: str) -> bool:
        return bool(VALID_EMAIL_PATTERN.fullmatch(email))
    
    return [email for email in strings if is_valid_email(email)]
