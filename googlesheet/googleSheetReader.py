from googleapiclient.errors import HttpError

class GoogleSheetReader:
    def __init__(self,spreadsheet_id, authenticator):
        self.spreadsheet_id = spreadsheet_id
        self.service = authenticator.credentials

    def get_keywords_from_sheet(self, range_name="keyword!A1:A10"):
        try:
            result=self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_name
            ).execute()
            values=result.get('values',[])

            if not values:
                print('no data found')
                return []
            return values
            
        except HttpError as err:
            print(f"an error occured:{err}")
            return []