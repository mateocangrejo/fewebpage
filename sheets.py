import os
import json
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2 import service_account
load_dotenv()

def read_sheets(sample_range):

    SERVICE_ACCOUNT_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID = '1xbJfHv4XNctvIJr3GiGkOKK5VNpvxa-45Owgr5LZyTs'

    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=sample_range).execute()
    values = result.get('values', [list])
    print(values)

SAMPLE_RANGE_NAME='Santifica el día!A1:I1'
#read_sheets(SAMPLE_RANGE_NAME)

def write_sheets(range_write, value_range):

    SERVICE_ACCOUNT_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    #creds = service_account.Credentials.from_service_account_file(
    #        SERVICE_ACCOUNT_FILE, scopes=SCOPES) #Old one

    json_str = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    #print(json_str)
    # generate json - if there are errors here remove newlines in .env
    json_data = json.loads(json_str)
    
    # the private_key needs to replace \n parsed as string literal with escaped newlines
    json_data['private_key'] = json_data['private_key'].replace('\\n', '\n')
    creds = service_account.Credentials.from_service_account_info(
        json_data)

    SAMPLE_SPREADSHEET_ID = '1xbJfHv4XNctvIJr3GiGkOKK5VNpvxa-45Owgr5LZyTs'

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=range_write,
                                    valueInputOption="USER_ENTERED",
                                    body=value_range).execute()

    print(request)

range_write='Santifica el día!A22'
list= [['aa',2],['ba',4]]

value_range={'values':list}

#write_sheets(range_write, value_range)
