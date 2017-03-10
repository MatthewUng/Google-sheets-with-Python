import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Test').sheet1

pp = pprint.PrettyPrinter()
result = sheet.get_all_records()
#result = sheet.row_values(1)
#result = sheet.col_values(1)
#result = sheet.cell(1,1).value
#sheet.update_cell(1,1, "updated")
#result = sheet.cell(1,1).value

#row = ["updating", "a", "row", "!!"]
#sheet.insert_row(row, 1)

#sheet.delete_row(1)
#print sheet.row_count

pp.pprint(result)

