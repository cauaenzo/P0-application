
import requests

from app.config import load_llm_config


class LLMClientError(Exception):
    """Representa erros durante a comunicação com o serviço de LLM."""


def prepare_request(system_prompt: str, user_text: str, config):
    """Prepara os dados necessários para a requisição."""

    endpoint = f"{config.base_url.rstrip('/')}/chat/completions"

    headers = {
        "Authorization": f"Bearer {config.api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": config.model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        "stream": False,
        "max_tokens": 2048
    }

    return endpoint, headers, payload


def parse_response(response) -> str:
    """Valida e extrai o conteúdo retornado pelo modelo."""

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


def generate_response(system_prompt: str, user_text: str) -> str:
    """Envia uma solicitação ao LLM e retorna sua resposta."""

    config = load_llm_config()

    endpoint, headers, payload = prepare_request(
        system_prompt,
        user_text,
        config
    )

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
        status_code = (
            error.response.status_code
            if error.response is not None
            else None
        )

        messages = {
            401: "A credencial de acesso é inválida.",
            403: "A credencial não possui autorização para acessar o serviço.",
            404: "O modelo ou endpoint solicitado não foi encontrado.",
            429: "O limite de requisições do serviço foi atingido.",
        }

        if status_code in messages:
            message = messages[status_code]
        elif status_code is not None and status_code >= 500:
            message = "O serviço de LLM está temporariamente indisponível."
        else:
            message = "O serviço de LLM recusou a solicitação."

        raise LLMClientError(message) from error

    except requests.exceptions.RequestException as error:
        raise LLMClientError(
            "Ocorreu um erro durante a comunicação com o serviço."
        ) from error

    return parse_response(response)
