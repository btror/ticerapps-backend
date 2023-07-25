import os
import smtplib
from email.message import EmailMessage

from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    sender_email = data.get('sender_email')
    message_body = data.get('message_body')

    if not sender_email or not message_body:
        return "Missing required data: sender_email or message_body", 400

    try:
        msg = EmailMessage()
        msg.set_content(message_body)

        email_address = os.getenv("EMAIL_ADDRESS")
        email_password = os.getenv("EMAIL_PASSWORD")

        msg['From'] = sender_email
        msg['To'] = email_address
        msg['Subject'] = 'New message from Flask API'

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(email_address, email_password)
            server.send_message(msg)

        return "Message sent successfully", 200

    except Exception as e:
        return f"An error occurred: {str(e)}", 500


app.run()
