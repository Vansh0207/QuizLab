from google_auth_oauthlib.flow import InstalledAppFlow
import json

# Define the scopes your app needs (modify if needed)
SCOPES = ['https://www.googleapis.com/auth/documents']

def main():
    # Load credentials from the credentials.json file
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)

    # Start the OAuth flow — opens a browser window
    creds = flow.run_local_server(port=8000)


    # Save the access + refresh token to token.json
    with open('token.json', 'w') as token_file:
        token_file.write(creds.to_json())

if __name__ == '__main__':
    main()
