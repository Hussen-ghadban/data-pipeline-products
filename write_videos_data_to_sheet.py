from googleapiclient.errors import HttpError
from authenticate import authenticate_google_sheets
import config
SPREADSHEET_ID=config.SPREADSHEET_ID_MULTIMEDIA_CONTENT_DATA
RANGE_NAME='multimedia!A1'
def write_youtube_data_to_sheet(youtube_data):
    service=authenticate_google_sheets()
    values=[ ["Title","Channel","Video Link","Description","Views","Likes","Publish Date"]]
    for video in youtube_data:
        values.append([
            video['title'],
            video['channel'],
            video['video_link'],
            video['description'],
            video['views'],
            video['likes'],
            video['publish_date']
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
