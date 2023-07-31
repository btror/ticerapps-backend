import os
import smtplib
from email.message import EmailMessage

from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from flask_basicauth import BasicAuth

load_dotenv()

PORT = 5000

app = Flask(__name__)
app.debug = False
CORS(app)

if os.environ.get("FLASK_ENV") != "production":
    load_dotenv()

# Optional configuration. Only required if basic_auth decorator is uncommented. Ignore otherwise.
app.config["BASIC_AUTH_USERNAME"] = os.environ.get("BASIC_AUTH_USERNAME")
app.config["BASIC_AUTH_PASSWORD"] = os.environ.get("BASIC_AUTH_PASSWORD")
basic_auth = BasicAuth(app)


@app.route("/send_message", methods=["POST"])
# @basic_auth.required  # Uncomment to require authentication for endpoint access
def send_message():
    data = request.get_json()
    sender_email = data.get("sender_email")
    message_body = data.get("message_body")

    if not sender_email or not message_body:
        return jsonify({"error": "Missing required data: sender_email or message_body"}), 400

    try:
        msg = EmailMessage()
        msg.set_content(message_body)

        email_address = os.environ.get("EMAIL_ADDRESS")
        email_password = os.environ.get("EMAIL_PASSWORD")

        msg["From"] = sender_email
        msg["To"] = email_address
        msg["Subject"] = "New message from Flask API"

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email_address, email_password)
            server.send_message(msg)

        return jsonify({"message": "Message sent successfully"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(threaded=True, port=int(os.environ.get("PORT", PORT)))
