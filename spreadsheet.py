import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Drive Backend-dcef73107445.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Test').sheet1

f = sheet.get_all_records()
print f
