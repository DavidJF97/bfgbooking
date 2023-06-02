import gspread
from google.oauth2.service_account import Credentials

# Set up credentials to access Google Sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the spreadsheet by its title
spreadsheet = CLIENT.open('BFGbookings')

# Select the worksheet you want to work with (e.g., 'Sheet1')
worksheet = spreadsheet.worksheet('responses')

# Get all values from the worksheet
data = worksheet.get_all_values()

# Iterate over the rows and display guest information room by room
for row in data[1:]:  # Skip the header row
    guest_name = row[0]
    email = row[1]
    check_in_date = row[2]
    check_out_date = row[3]
    room_type = row[4]
    additional_notes = row[5]

    # Perform any desired processing or display the guest information
    print(f"Guest Name: {guest_name}")
    # print(f"Email: {email}")
    # print(f"Check-in Date: {check_in_date}")
    # print(f"Check-out Date: {check_out_date}")
    # print(f"Room Type: {room_type}")
    # print(f"Additional Notes: {additional_notes}")
