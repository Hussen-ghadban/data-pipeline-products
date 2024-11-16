import os
import json
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

class GoogleSheetAuthenticator:
    #define the scopes for accessing google sheets API
    SCOPES=['https://www.googleapis.com/auth/spreadsheets']

    def __init__(self):
        #Initialize the authentication for google sheet
        self.credentials = self._authenticate_google_sheets()

    def _authenticate_google_sheets(self):
        creds=None
        #check if token.json exist to load saved credentials
        if os.path.exists('token.json'):
            with open('token.json','r') as token:
                token_data=json.load(token)
            # load data from token.json
            creds = Credentials(
                token=token_data['token'],
                refresh_token=token_data['refresh_token'],
                token_uri=token_data['token_uri'],
                client_id=token_data['client_id'],
                client_secret=token_data['client_secret'],
                scopes=token_data['scopes'],
            )

        # if there are no valid credentials, refresh or obtain new ones
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except RefreshError as e:
                    print(f"Error refresghin token:{e}")
                    creds=None
            else:
                # if no valid credentials, initiate OAuth flows
                flow=InstalledAppFlow.from_client_secrets_file('credentials.json',self.SCOPES)
                
                creds=flow.run_local_server(port=0)

                # save the new credentials to token.json
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
                # write the new or updated credentials into token.json 
            with open('token.json','w') as token:
                json.dump(modified_token,token,indent=4)
        # create a google sheet service object
        service=build('sheets','v4',credentials=creds)
        return service