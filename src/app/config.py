import os
from dataclasses import dataclass
from urllib.parse import urlsplit

from dotenv import load_dotenv


class ConfigurationError(ValueError):
    """Representa erros na configuração de acesso ao LLM."""


@dataclass(frozen=True)
class LLMConfig:
    api_key: str
    base_url: str
    model: str


def load_llm_config() -> LLMConfig:
    """Carrega e valida as configurações necessárias para acessar o LLM."""

    load_dotenv()

    api_key = os.getenv("LLM_API_KEY", "").strip()
    base_url = os.getenv("LLM_BASE_URL", "").strip()
    model = os.getenv("LLM_MODEL", "").strip()

    if not api_key:
        raise ConfigurationError(
            "A credencial de acesso não foi configurada. "
            "Defina LLM_API_KEY no arquivo .env."
        )

    if not base_url:
        raise ConfigurationError(
            "O endereço do serviço não foi configurado. "
            "Defina LLM_BASE_URL no arquivo .env."
        )

    parsed_url = urlsplit(base_url)

    if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
        raise ConfigurationError(
            "O endereço do serviço é inválido. "
            "Verifique o valor de LLM_BASE_URL."
        )

    if not model:
        raise ConfigurationError(
            "O modelo de LLM não foi configurado. "
            "Defina LLM_MODEL no arquivo .env."
        )

    return LLMConfig(
        api_key=api_key,
        base_url=base_url.rstrip("/"),
        model=model
    )