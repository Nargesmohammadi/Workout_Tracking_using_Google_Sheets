# Workout_Tracking_using_Google_Sheets

This is a simple workout tracking program that uses Google Sheets as its database. The application is written in Python and utilizes the Google Sheets API to read from and write to the spreadsheet.

## Usage

- Before running the code, you need to have a Google account and create a new Google Sheet for your workout data.
- Follow the instructions in [Google Sheets API Quickstart](https://developers.google.com/sheets/api/quickstart/python) to enable the Google Sheets API and download the `credentials.json` file.
- Copy the `credentials.json` file to the project directory.
- Open `config.py` and fill in the required fields:
  - `SPREADSHEET_ID`: The ID of your Google Sheet (found in the URL).
  - `RANGE_NAME`: The range of cells where your data will be stored (e.g. `"Sheet1!A:B"` for columns A and B in the first sheet).
- Run the program: `python main.py`

The program will prompt you to enter your workout data and store it in the Google Sheet.
