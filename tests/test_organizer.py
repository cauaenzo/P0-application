import unittest
from unittest.mock import patch

from app.organizer import organize_note
from app.prompts import SYSTEM_PROMPT


class TestOrganizer(unittest.TestCase):

    @patch("app.organizer.generate_response")
    def test_organize_note(self, mock_generate):
        mock_generate.return_value = "Anotação organizada"

        result = organize_note("  Reunião amanhã às 14h.  ")

        self.assertEqual(result, "Anotação organizada")
        mock_generate.assert_called_once_with(
            SYSTEM_PROMPT,
            "Reunião amanhã às 14h."
        )

    def test_reject_empty_note(self):
        with self.assertRaises(ValueError):
            organize_note("   ")


if __name__ == "__main__":
    unittest.main()