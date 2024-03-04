from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = 'keys.json' #replace with the key file name that you downloaded

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = "11o-ZoNmn4-FdCHd0gJuZMrUC-3mYFgo2EheHKIJfhvE" #Give the ID of the Google spreadsheet


def append_data(value):
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        
        result = (
            sheet.values()
            .append(spreadsheetId=SPREADSHEET_ID, range="camera!A1", 
                    valueInputOption="USER_ENTERED",
                    insertDataOption="INSERT_ROWS",
                    body = {"values": value})
            .execute()
        )
        
        
    except HttpError as err:
        print(err)

value = [["24/03/2024 9:22:00", "20","11","3","15"]]
append_data(value)
