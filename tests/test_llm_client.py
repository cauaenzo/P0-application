
import unittest
from unittest.mock import Mock, patch

import requests

from app.llm_client import (
    generate_response,
    LLMClientError,
    prepare_request,
    parse_response
)


class TestLLMClient(unittest.TestCase):

    def test_prepare_request(self):
        config = Mock(
            api_key="chave-de-teste",
            base_url="https://example.com/v1/",
            model="modelo-teste"
        )

        endpoint, headers, payload = prepare_request(
            "Prompt do sistema",
            "Minha anotação",
            config
        )

        self.assertEqual(
            endpoint,
            "https://example.com/v1/chat/completions"
        )
        self.assertEqual(
            headers["Authorization"],
            "Bearer chave-de-teste"
        )
        self.assertEqual(payload["model"], "modelo-teste")
        self.assertEqual(
            payload["messages"][1]["content"],
            "Minha anotação"
        )

    @patch("app.llm_client.load_llm_config")
    @patch("app.llm_client.requests.post")
    def test_successful_response(self, mock_post, mock_config):
        mock_config.return_value = Mock(
            api_key="chave-de-teste",
            base_url="https://example.com/v1",
            model="modelo-teste"
        )

        mock_response = Mock()
        mock_response.json.return_value = {
            "choices": [
                {"message": {"content": "Nota organizada"}}
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = generate_response("Prompt", "Minha anotação")

        self.assertEqual(result, "Nota organizada")
        mock_post.assert_called_once()

    @patch("app.llm_client.load_llm_config")
    @patch("app.llm_client.requests.post")
    def test_invalid_credentials(self, mock_post, mock_config):
        mock_config.return_value = Mock(
            api_key="chave-de-teste",
            base_url="https://example.com/v1",
            model="modelo-teste"
        )

        response = Mock()
        response.status_code = 401

        mock_post.side_effect = requests.exceptions.HTTPError(
            response=response
        )

        with self.assertRaises(LLMClientError) as context:
            generate_response("Prompt", "Anotação")

        self.assertEqual(
            str(context.exception),
            "A credencial de acesso é inválida."
        )
        self.assertNotIn(
            "chave-de-teste",
            str(context.exception)
        )

    @patch("app.llm_client.load_llm_config")
    @patch("app.llm_client.requests.post")
    def test_model_unavailable(self, mock_post, mock_config):
        mock_config.return_value = Mock(
            api_key="chave-de-teste",
            base_url="https://example.com/v1",
            model="modelo-teste"
        )

        response = Mock()
        response.status_code = 404

        mock_post.side_effect = requests.exceptions.HTTPError(
            response=response
        )

        with self.assertRaises(LLMClientError):
            generate_response("Prompt", "Anotação")

    @patch("app.llm_client.load_llm_config")
    @patch("app.llm_client.requests.post")
    def test_rate_limit(self, mock_post, mock_config):
        mock_config.return_value = Mock(
            api_key="chave-de-teste",
            base_url="https://example.com/v1",
            model="modelo-teste"
        )

        response = Mock()
        response.status_code = 429

        mock_post.side_effect = requests.exceptions.HTTPError(
            response=response
        )

        with self.assertRaises(LLMClientError):
            generate_response("Prompt", "Anotação")

    @patch("app.llm_client.load_llm_config")
    @patch("app.llm_client.requests.post")
    def test_server_error(self, mock_post, mock_config):
        mock_config.return_value = Mock(
            api_key="chave-de-teste",
            base_url="https://example.com/v1",
            model="modelo-teste"
        )

        response = Mock()
        response.status_code = 503

        mock_post.side_effect = requests.exceptions.HTTPError(
            response=response
        )

        with self.assertRaises(LLMClientError):
            generate_response("Prompt", "Anotação")

    @patch("app.llm_client.load_llm_config")
    @patch("app.llm_client.requests.post")
    def test_timeout(self, mock_post, mock_config):
        mock_config.return_value = Mock(
            api_key="chave-de-teste",
            base_url="https://example.com/v1",
            model="modelo-teste"
        )

        mock_post.side_effect = requests.exceptions.Timeout

        with self.assertRaisesRegex(
            LLMClientError,
            "demorou demais"
        ):
            generate_response("Prompt", "Anotação")

    @patch("app.llm_client.load_llm_config")
    @patch("app.llm_client.requests.post")
    def test_connection_error(self, mock_post, mock_config):
        mock_config.return_value = Mock(
            api_key="chave-de-teste",
            base_url="https://example.com/v1",
            model="modelo-teste"
        )

        mock_post.side_effect = requests.exceptions.ConnectionError

        with self.assertRaisesRegex(
            LLMClientError,
            "Não foi possível conectar"
        ):
            generate_response("Prompt", "Anotação")

    @patch("app.llm_client.load_llm_config")
    @patch("app.llm_client.requests.post")
    def test_empty_response(self, mock_post, mock_config):
        mock_config.return_value = Mock(
            api_key="chave-de-teste",
            base_url="https://example.com/v1",
            model="modelo-teste"
        )

        response = Mock()
        response.json.return_value = {
            "choices": [
                {"message": {"content": "   "}}
            ]
        }
        response.raise_for_status.return_value = None
        mock_post.return_value = response

        with self.assertRaisesRegex(
            LLMClientError,
            "resposta vazia"
        ):
            generate_response("Prompt", "Anotação")

    @patch("app.llm_client.load_llm_config")
    @patch("app.llm_client.requests.post")
    def test_unexpected_response(self, mock_post, mock_config):
        mock_config.return_value = Mock(
            api_key="chave-de-teste",
            base_url="https://example.com/v1",
            model="modelo-teste"
        )

        response = Mock()
        response.json.return_value = {"unexpected": "structure"}
        response.raise_for_status.return_value = None
        mock_post.return_value = response

        with self.assertRaisesRegex(
            LLMClientError,
            "interpretar a resposta"
        ):
            generate_response("Prompt", "Anotação")

    def test_parse_valid_response(self):
        response = Mock()
        response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "  Nota organizada  "
                    }
                }
            ]
        }

        result = parse_response(response)

        self.assertEqual(result, "Nota organizada")

    def test_invalid_json_response(self):
        response = Mock()
        response.json.side_effect = ValueError("Invalid JSON")

        with self.assertRaisesRegex(
            LLMClientError,
            "interpretar a resposta"
        ):
            parse_response(response)


if __name__ == "__main__":
    unittest.main()
