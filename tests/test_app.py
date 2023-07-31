import unittest
from unittest.mock import patch
from main.app import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch("smtplib.SMTP_SSL")
    def test_send_message_success(self, mock_smtp):
        instance = mock_smtp.return_value
        instance.login.return_value = None

        data = {
            "sender_email": "sender@example.com",
            "message_body": "Test message body"
        }

        response = self.app.post("/send_message", json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Message sent successfully"})

    @patch('smtplib.SMTP_SSL')
    def test_send_message_missing_data(self, mock_smtp):
        instance = mock_smtp.return_value
        instance.login.return_value = None

        data = {
            "message_body": "Test message body"
        }

        response = self.app.post("/send_message", json=data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Missing required data: sender_email or message_body"})


if __name__ == "__main__":
    unittest.main()
