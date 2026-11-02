
import os

import requests
from dotenv import load_dotenv


load_dotenv()


class LLMClientError(Exception):
    """Representa erros durante a comunicação com o serviço de LLM."""


def get_llm_configuration():
    """Carrega e valida as configurações necessárias para acessar o LLM."""

    api_key = os.getenv("LLM_API_KEY")
    base_url = os.getenv("LLM_BASE_URL")
    model = os.getenv("LLM_MODEL")

    if not api_key:
        raise LLMClientError("A variável LLM_API_KEY não foi configurada.")

    if not base_url:
        raise LLMClientError("A variável LLM_BASE_URL não foi configurada.")

    if not model:
        raise LLMClientError("A variável LLM_MODEL não foi configurada.")

    return api_key, base_url.rstrip("/"), model


def generate_response(system_prompt: str, user_text: str) -> str:
    """Envia um texto ao LLM e retorna o conteúdo da resposta."""

    api_key, base_url, model = get_llm_configuration()

    endpoint = f"{base_url}/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_text
            }
        ],
        "stream": False,
        "max_tokens": 2048
    }

    try:
        response = requests.post(
            endpoint,
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

    except requests.exceptions.Timeout as error:
        raise LLMClientError(
            "O serviço de LLM demorou demais para responder."
        ) from error

    except requests.exceptions.ConnectionError as error:
        raise LLMClientError(
            "Não foi possível conectar ao serviço de LLM."
        ) from error

    except requests.exceptions.HTTPError as error:
        raise LLMClientError(
            f"O serviço retornou um erro HTTP: {error.response.status_code}."
        ) from error

    except requests.exceptions.RequestException as error:
        raise LLMClientError(
            "Ocorreu um erro durante a requisição."
        ) from error

    try:
        data = response.json()

        content = data["choices"][0]["message"]["content"]

    except (ValueError, KeyError, IndexError, TypeError) as error:
        raise LLMClientError(
            "Não foi possível interpretar a resposta do modelo."
        ) from error

    if not isinstance(content, str) or not content.strip():
        raise LLMClientError(
            "O modelo retornou uma resposta vazia ou inválida."
        )

    return content.strip()
