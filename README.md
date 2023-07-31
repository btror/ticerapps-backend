# ticerapps-backend
## About

This is a simple Flask web application that serves as an email notifier. When a user visits ticerapps.com and fills out the contact form with their email address and a message, the application sends an email to the specified email address using the configured email server.

## Setup and Configuration

Before running the application, ensure you have Python and Flask installed on your system. Additionally, you will need to set up the necessary environment variables.

## Environment Variables

The application uses environment variables to store sensitive information and configuration. Create a .env file in the root directory and add the following environment variables:

- FLASK_ENV: Set this to production in production environments.
- EMAIL_ADDRESS: The email address used as the sender for the notifications.
- EMAIL_PASSWORD: The password for the sender email account.
- PORT: The port number for the Flask application to run (default is 5000).

### Optional Variables

- BASIC_AUTH_USERNAME: The username for basic authentication when accessing the /send_message endpoint. Set this to add a basic authentication layer to your API (uncomment basic_auth.required on endpoint to use).
- BASIC_AUTH_PASSWORD: The password for basic authentication when accessing the /send_message endpoint (uncomment basic_auth.required on endpoint to use).

## Running the Application

Once you have set up the environment variables, you can run the application using the following command:
python app.py

The application will start running on the specified port (default is 5000) and will be accessible at http://localhost:PORT/.

## Usage

To use the application, simply make a POST request to the /send_message endpoint with the following JSON data:

{
  "sender_email": "user@example.com",
  "message_body": "This is a test message."
}

Ensure you have set up the proper CORS configuration to allow cross-origin requests if accessing the API from a different domain.

When the request is successful, the application will send an email notification to the specified email address with the provided message.

In case of any errors, the application will respond with the appropriate error message.

Note: Ensure that the EMAIL_ADDRESS used for the sender email has the necessary permissions to send emails via the configured SMTP server.

Feel free to modify the application as needed to suit your specific requirements.