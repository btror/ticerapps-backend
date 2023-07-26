import unittest
import requests
from unittest.mock import patch


class TestApp(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000"

    @patch("requests.post")
    def test_send_message(self, mock_post):
        data = {
            "sender_email": "sender@example.com",
            "message_body": "test message",
        }
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.text = "Message sent successfully"

        response = requests.post(f"{self.BASE_URL}/send_message", json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent successfully")


if __name__ == "__main__":
    unittest.main()
