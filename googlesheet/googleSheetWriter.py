from googleapiclient.errors import HttpError
from googleSheetReader import GoogleSheetReader
class GoogleSheetWriter:
    def __init__(self, spreadsheet_id, range_name, authenticator):
        self.spreadsheet_id = spreadsheet_id
        self.range_name = range_name
        self.service = authenticator.credentials
        self.reader = GoogleSheetReader(spreadsheet_id, authenticator)

    def write_data_to_sheet(self, data, headers):
        
        existing_data = self.reader.get_keywords_from_sheet(self.range_name)
        if not existing_data:
            values=[headers] + [list(item.values()) for item in data]
        else:
            values = [list(item.values()) for item in data]

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
