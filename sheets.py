#→ Google Sheets operations
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("ExpenseTracker").sheet1

def add_expense(amount, desc, user):
    now = datetime.now()

    row = [
        now.strftime("%Y-%m-%d"),
        now.strftime("%b-%Y"),
        user,
        amount,
        desc
    ]

    sheet.append_row(row)

def get_summary(month):
    records = sheet.get_all_records()

    filtered = [r for r in records if r["Month-Year"] == month]

    total = sum(int(r["Amount"]) for r in filtered)

    return total, filtered