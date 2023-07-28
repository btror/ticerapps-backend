# ticerapps-backend
## About

This is a simple Flask web application that serves as an email notifier. When a user visits [ticerapps.com](https://ticerapps.com) and fills out the contact form with their email address and a message, the application sends an email to the specified email address using the configured email server.

## Setup and Configuration

Before running the application, ensure you have Python and Flask installed on your system. Additionally, you will need to set up the necessary environment variables.

## Environment Variables

The application uses environment variables to store sensitive information and configuration. Create a .env file in the root directory and add the following environment variables:

- ```FLASK_ENV``` set this to production in production environments.
- ```BASIC_AUTH_USERNAME``` (optional) username for basic authentication when accessing the /send_message endpoint.
- ```BASIC_AUTH_PASSWORD``` (optional) password for basic authentication when accessing the /send_message endpoint.
- ```EMAIL_ADDRESS``` email address used as the sender for the notifications.
- ```EMAIL_PASSWORD``` password for the sender email account.
- ```PORT``` port number for the Flask application to run (default is 5000).

## Running the Application

Once you have set up the environment variables, you can run the application using the following command:

```bash
python app.py
```

The application will start running on the specified port (default is 5000) and will be accessible at ```http://localhost:<PORT>```

## Usage

To use the application, simply make a POST request to the /send_message endpoint with the following JSON data:
```json
{
  "sender_email": "user@example.com",
  "message_body": "A message to send."
}
```
- Ensure you have set up the proper CORS configuration to allow cross-origin requests if accessing the API from a different domain.
- When the request is successful, the application will send an email notification to the specified email address with the provided message.
- In case of any errors, the application will respond with the appropriate error message.
- Ensure that the ```EMAIL_ADDRESS``` used for the sender email has the necessary permissions to send emails via the configured SMTP server.

## Live Deployment

Steps to deploy backend on Heroku:
- Connect repository to Heroku.
- Create config vars for all environment variables listed above.
- Create environment.prod.ts file in src/environments in frontend Angular app:
```typescript
export const environment = {
  production: true,
  apiUrl: '<heroku URL>/send_message',
};
```
- Adjust angular.json file in frontend Angular to use production environment:
```json
"configurations": {
  "production": {
    "fileReplacements": [
      {
        "replace": "src/environments/environment.ts",
        "with": "src/environments/environment.prod.ts"
      }
    ],
    ...
  }
  ...
}
```
- <B>NOTE</B> github pages <I>sadly</I> does not support POST requests, so this will not work if the frontend Angular app is hosted there...

## ticerapps-v2 (Angular frontend)

View frontend code at [btror/ticerapps-v2](https://github.com/btror/ticerapps-v2).

View live at [ticerapps.com](https://ticerapps.com).

Feel free to modify the application as needed to suit your specific requirements.
