import requests
from datetime import datetime

N_API_KEY = ""
N_APP_ID = ""

sheet_endpoint = "https://api.sheety.co/f7517ad33ca76c0452786a377a26331f/workoutTracking/sheet1"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me witch exercises you did today?: ")

exercise_headers = {
    "x-app-id": "e3e62c62",
    "x-app-key": "3243e3259727c2e5375c70d655a1fbe7",
}

params = {
    "query": exercise_text,
}

response = requests.post(url=exercise_endpoint, json=params, headers=exercise_headers)
result = response.json()

today = datetime.now().strftime("%Y%m%d")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_input)
    print(sheet_response)

