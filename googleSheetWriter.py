from googleapiclient.errors import HttpError

class GoogleSheetWriter:
    def __init__(self, spreadsheet_id, range_name, authenticator):
        self.spreadsheet_id = spreadsheet_id
        self.range_name = range_name
        self.service = authenticator.credentials

    def write_data_to_sheet(self, data, headers):
        values=[headers] + [list(item.values()) for item in data]

        body={
                'values':values
            }
        try:
            result=self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=self.range_name,
                valueInputOption="RAW",
                body=body
            ).execute()
            print(f"{result.get('updatedCells')} cells updated.")
        except HttpError as error:
            print(f"an error occured:{error}")
