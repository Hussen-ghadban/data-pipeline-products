import os
import json
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES=['https://www.googleapis.com/auth/spreadsheets.readonly']

def authenticate_google_sheets():
    creds=None
    if os.path.exists('token.json'):
        creds=Credentials.from_authorized_user_file('token.json',SCOPES)
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

        with open('token.json','w') as token:
            json.dump(creds.to_json(),token)

    service=build('sheets','v4',credentials=creds)
    return service