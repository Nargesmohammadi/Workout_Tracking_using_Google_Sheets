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

## Methods

### `authenticate_google()`

This method authenticates the user's credentials by creating a flow object and launching a web server to request authorization from the user.

### `get_workout_data()`

This method prompts the user to input their workout data (date, exercise, and duration) and returns it as a list.

### `add_workout_data(sheets_api, spreadsheet_id, range_name, workout_data)`

This method adds a new row to the Google Sheet with the workout data specified by the user.

### `main()`

This method serves as the entry point to the program. It calls the above methods in sequence to authenticate the user, get the workout data, and add it to the Google Sheet.

## Dependencies

- `google-auth`
- `google-auth-oauthlib`
- `google-auth-httplib2`
- `google-api-python-client`
