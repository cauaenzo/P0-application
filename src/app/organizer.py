from app.llm_client import generate_response
from app.prompts import SYSTEM_PROMPT


def organize_note(note: str) -> str:
    if not note or not note.strip():
        raise ValueError("A anotação não pode estar vazia.")

    return generate_response(SYSTEM_PROMPT, note.strip())