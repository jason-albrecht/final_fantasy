from dataclasses import dataclass

@dataclass
class Text:
    text: str

    def capitalize(text: str) -> str:
        return text.upper()