import os
import json
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES=['https://www.googleapis.com/auth/spreadsheets']

def authenticate_google_sheets():
    creds=None
    if os.path.exists('token.json'):
        with open('token.json','r') as token:
            token_data=json.load(token)

        creds = Credentials(
            token=token_data['token'],
            refresh_token=token_data['refresh_token'],
            token_uri=token_data['token_uri'],
            client_id=token_data['client_id'],
            client_secret=token_data['client_secret'],
            scopes=token_data['scopes'],
        )
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError as e:
                print(f"Error refresghin token:{e}")
                creds=None
        else:
            flow=InstalledAppFlow.from_client_secrets_file('credentials.json',SCOPES)
            creds=flow.run_local_server(port=0)

            modified_token = {
                "token": creds.token,
                "refresh_token": creds.refresh_token,
                "token_uri": creds.token_uri,
                "client_id": creds.client_id,
                "client_secret": creds.client_secret,
                "scopes": creds.scopes,
                "universe_domain": "googleapis.com",
                "account": "",
                "expiry": creds.expiry.isoformat()
            }
        with open('token.json','w') as token:
            json.dump(modified_token,token,indent=4)

    service=build('sheets','v4',credentials=creds)
    return service