from datetime import date
import logging
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(dir_path, "client_secret.json"), scope)
gc = gspread.authorize(creds)

workbook = os.environ["workbook"]  # TODO: Hard-code your created Google Sheet name
wks_name = os.environ.get("worksheet")  # TODO: Enter worksheet Preferably do not use "Sheet1"

logger.info(f"Opening {workbook}")

gsheet = gc.open(workbook)

HEADERS = ["Header 1", "Header 2", "Header 3"]   # TODO: Add headers

if __name__ == "__main__":
    try:
        logger.info(f"Fetching information at {date.today()}")

        # Fetch the worksheet, create it with headers if it does not exist 
        try:
            wks = gsheet.worksheet(wks_name)
            logger.info("Fetched worksheet")
        except gspread.exceptions.WorksheetNotFound:
            wks = gsheet.add_worksheet(title=wks_name, rows=1, cols=len(HEADERS))
            wks.append_row(HEADERS)
            logger.info(f"{wks_name} sheet was created")

        row = ["Data 1", "Data 2", "Data 3 "]  # The data added onto the Google Sheet
        wks.append_row(row)

        logger.info(f"Row written to {wks_name}")
    except Exception as e:
        print(e)

