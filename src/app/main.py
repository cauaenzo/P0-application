from app.organizer import organize_note
from app.llm_client import LLMClientError


def main():
    print("=== Organizador de Anotações ===")

    note = input("\nDigite sua anotação:\n> ").strip()

    if not note:
        print("\nA anotação não pode estar vazia.")
        return

    try:
        result = organize_note(note)
    except (LLMClientError, ValueError) as error:
        print(f"\nErro: {error}")
        return

    print("\n=== Anotação organizada ===\n")
    print(result)


if __name__ == "__main__":
    main()