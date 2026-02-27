import re
import unicodedata



def sanitize_name(name: str) -> str:
    name = unicodedata.normalize("NFD", name)
    name = name.encode("ascii", "ignore").decode("ascii")
    name = name.lower()
    name = re.sub(r'[^a-z]+', '_', name)
    name = name.strip("_")
    return name