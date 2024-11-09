from googleapiclient.errors import HttpError
from authenticate import authenticate_google_sheets
import config
SPREADSHEET_ID=config.SPREADSHEET_ID_PRODUCT_DATA
RANGE_NAME='productData!A1'
def write_aliexpress_data_to_sheet(aliexpress_data):
    service=authenticate_google_sheets()
    values=[ ["Title","Description","Product Link","Price","Website Source"]]
    for data in aliexpress_data:
        values.append([
            data['Title'],
            data['Description'],
            data['Product Link'],
            data['Price'],
            data['Website Source'],
        ])

    body={
            'values':values
        }
    try:
        result=service.spreadsheets().values().update(
              spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption="RAW",
            body=body
        ).execute()
        print(f"{result.get('updatedCells')} cells updated.")
    except HttpError as error:
        print(f"an error occured:{error}")
