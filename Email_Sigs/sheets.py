from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pandas as pd
import gspread


# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = 'Your Spreadsheet'
RANGE_NAME = 'Your Sheet Name'


""" Retrieve sheet data using OAuth credentials and Google Python API. """
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

CLIENT_SECRET = 'client_secret.json'

store = file.Storage('credentials_drive_matt.json') #obviously, I've removed the json files from this project
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
    creds = tools.run_flow(flow, store)

service = build('sheets', 'v4', http=creds.authorize(Http()))

# Call the Sheets API
gsheet = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()


def gsheet2df(gsheet):
    """ Converts Google sheet data to a Pandas DataFrame.
    Note: This script assumes that your data contains a header file on the first row!
    Also note that the Google API returns 'none' from empty cells - in order for the code
    below to work, you'll need to make sure your sheet doesn't contain empty cells,
    or update the code to account for such instances.
    """
    header = gsheet.get('values', [])[0]   # Assumes first line is header!
    values = gsheet.get('values', [])[1:]  # Everything else is data.
    if not values:
        print('No data found.')
    else:
        all_data = []
        for col_id, col_name in enumerate(header):
            column_data = []
            for row in values:
                column_data.append(row[col_id])
            ds = pd.Series(data=column_data, name=col_name)
            all_data.append(ds)
        df = pd.concat(all_data, axis=1)
        return df


gsheet = get_google_sheet(SPREADSHEET_ID, RANGE_NAME)

df = gsheet2df(gsheet)
print('Dataframe size = ', df.shape)