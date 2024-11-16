from googleapiclient.errors import HttpError

class GoogleSheetReader:
    def __init__(self,spreadsheet_id, authenticator):
        self.spreadsheet_id = spreadsheet_id
        #Initializing the authentication
        self.service = authenticator.credentials

    def get_keywords_from_sheet(self, range_name="keyword!A1:A10"):
        try:
            # fetch data from the specified range in the google sheet 
            result=self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=range_name
            ).execute()
            values=result.get('values',[])
            return values
            
        except HttpError as err:
            print(f"an error occured:{err}")
            return []