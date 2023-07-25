import unittest
import requests


class TestApp(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000"

    def test_send_message(self):
        data = {
            "sender_email": "sender@example.com",
            "message_body": "test message",
        }
        response = requests.post(f"{self.BASE_URL}/send_message", json=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Message sent successfully")


if __name__ == "__main__":
    unittest.main()
