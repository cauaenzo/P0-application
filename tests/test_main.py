
import unittest
from unittest.mock import patch

from app.main import main
from app.config import ConfigurationError
from app.llm_client import LLMClientError


class TestMain(unittest.TestCase):

    @patch("app.main.print")
    @patch("app.main.organize_note")
    @patch("builtins.input", return_value="Minha anotação")
    def test_successful_execution(
        self,
        mock_input,
        mock_organize,
        mock_print
    ):
        mock_organize.return_value = "Nota organizada"

        main()

        mock_organize.assert_called_once_with("Minha anotação")
        mock_print.assert_any_call("Nota organizada")

    @patch("app.main.print")
    @patch("app.main.organize_note")
    @patch("builtins.input", return_value="   ")
    def test_reject_empty_input(
        self,
        mock_input,
        mock_organize,
        mock_print
    ):
        main()

        mock_organize.assert_not_called()
        mock_print.assert_any_call(
            "\nA anotação não pode estar vazia."
        )

    @patch("app.main.print")
    @patch("app.main.organize_note")
    @patch("builtins.input", return_value="Minha anotação")
    def test_configuration_error(
        self,
        mock_input,
        mock_organize,
        mock_print
    ):
        mock_organize.side_effect = ConfigurationError(
            "Credencial não configurada."
        )

        main()

        mock_print.assert_any_call(
            "\nErro: Credencial não configurada."
        )

    @patch("app.main.print")
    @patch("app.main.organize_note")
    @patch("builtins.input", return_value="Minha anotação")
    def test_llm_client_error(
        self,
        mock_input,
        mock_organize,
        mock_print
    ):
        mock_organize.side_effect = LLMClientError(
            "Não foi possível conectar ao serviço de LLM."
        )

        main()

        mock_print.assert_any_call(
            "\nErro: Não foi possível conectar ao serviço de LLM."
        )


if __name__ == "__main__":
    unittest.main()
