from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1wkaKyBaYxRxpyZhMb0doI5QQk6h0gLZdYS7vE8340iE'

SAMPLE_RANGE_NAME='Santifica el día!A1:I1'
range_write='Santifica el día!A22'

list= [['a',2],['b',4]]

service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [list])
value_range={'values':list}
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=range_write, valueInputOption="USER_ENTERED",body=value_range).execute()

print(values)
"""
if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[4]))
"""
