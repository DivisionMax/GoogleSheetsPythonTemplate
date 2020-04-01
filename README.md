# Google Sheet with Python Template

_Created: 1 April 2020_

Requires Python 3.6 or greater because f-strings

- Create a new worksheet, add and record the worksheet name
- Set up your Google Sheets API, I find [this tutorial](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html) the most straight-forward
- Create your credentials and download the `client_secret.json`
- You'll need the the `client_email` in the file
- Share the worksheet with the `client_email`
- By default; the template looks for the secrets file at the same level, but this is easily changed
- Follow the `TODO`s and comments in the template
