"""
This module retrieves and displays guest information from a Google Sheets
spreadsheet.
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('BFGbookings')

responses = SHEET.worksheet('responses')

data = responses.get_all_values()

# Prompt the user to enter the guest's name for search
print("Welcome to THE BUTTERFLY GUESTHOUSE guestbook\n")
while True:
    guest_name_to_search = input("""Enter the name of the guest the booking was made with:
(Or type 'exit' to leave)\n""")
    if guest_name_to_search.lower() == "exit":
        print("Exiting the program.")
        break

    guest_found = False

    for row in data[1:]:
        guest_name = row[1]

        if guest_name == guest_name_to_search:
            response_date = row[0]
            email = row[2]
            check_in_date = row[3]
            check_out_date = row[4]
            room_type = row[5]
            additional_notes = row[6]

            print("---")
            print(f"Guest Name: {guest_name}")
            print(f"Submit Date: {response_date}")
            print(f"Email: {email}")
            print(f"Check-in Date: {check_in_date}")
            print(f"Check-out Date: {check_out_date}")
            print(f"Room Type: {room_type}")
            print(f"Additional Notes: {additional_notes}")
            print("---")

            guest_found = True
            break

    if not guest_found:
        print("Guest not found. Please try again.")
