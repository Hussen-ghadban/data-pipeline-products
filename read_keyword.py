from authenticate import authenticate_google_sheets
from googleapiclient.errors import HttpError

import config
SPREADSHEET_ID=config.SPREADSHEET_ID_USER_INPUT
RANGE_NAME='keyword!A1:A10'

def get_keywords_from_sheet():
    service=authenticate_google_sheets()
    try:
        result=service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME
        ).execute()
        values=result.get('values',[])

        if not values:
            print('no data found')
        else:
            print('keywords retrieved:')
            for row in values:
                print(row[0])
    except HttpError as err:
        print(f"an error occured:{err}")