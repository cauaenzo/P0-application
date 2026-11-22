import os
import unittest
from unittest.mock import patch

from app.config import ConfigurationError, load_llm_config


class TestLLMConfig(unittest.TestCase):

    @patch("app.config.load_dotenv")
    def test_missing_api_key(self, mock_load_dotenv):
        environment = {
            "LLM_API_KEY": "",
            "LLM_BASE_URL": "https://integrate.api.nvidia.com/v1",
            "LLM_MODEL": "nvidia/nemotron-3.5-super-vl-120b-a12b"
        }

        with patch.dict(os.environ, environment, clear=True):
            with self.assertRaisesRegex(
                ConfigurationError,
                "credencial de acesso não foi configurada"
            ):
                load_llm_config()

    @patch("app.config.load_dotenv")
    def test_invalid_base_url(self, mock_load_dotenv):
        environment = {
            "LLM_API_KEY": "chave-de-teste",
            "LLM_BASE_URL": "endereco-invalido",
            "LLM_MODEL": "modelo-de-teste"
        }

        with patch.dict(os.environ, environment, clear=True):
            with self.assertRaisesRegex(
                ConfigurationError,
                "endereço do serviço é inválido"
            ):
                load_llm_config()

    @patch("app.config.load_dotenv")
    def test_missing_model(self, mock_load_dotenv):
        environment = {
            "LLM_API_KEY": "chave-de-teste",
            "LLM_BASE_URL": "https://integrate.api.nvidia.com/v1",
            "LLM_MODEL": " "
        }

        with patch.dict(os.environ, environment, clear=True):
            with self.assertRaisesRegex(
                ConfigurationError,
                "modelo de LLM não foi configurado"
            ):
                load_llm_config()

    @patch("app.config.load_dotenv")
    def test_load_valid_configuration(self, mock_load_dotenv):
        environment = {
            "LLM_API_KEY": "chave-de-teste",
            "LLM_BASE_URL": "https://integrate.api.nvidia.com/v1/",
            "LLM_MODEL": "nvidia/nemotron-3.5-super-vl-120b-a12b"
        }

        with patch.dict(os.environ, environment, clear=True):
            config = load_llm_config()

        self.assertEqual(config.api_key, "chave-de-teste")
        self.assertEqual(
            config.base_url,
            "https://integrate.api.nvidia.com/v1"
        )
        self.assertEqual(
            config.model,
            "nvidia/nemotron-3.5-super-vl-120b-a12b"
        )


if __name__ == "__main__":
    unittest.main()