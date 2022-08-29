import requests
from datetime import datetime


API_KEY = ""
APP_ID = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me witch exercises you did today?: ")

exercise_headers = {
    "x-app-id": "e3e62c62",
    "x-app-key": "3243e3259727c2e5375c70d655a1fbe7",
}

params = {
    "query": exercise_text,
}

today = datetime.now()

response = requests.post(url=exercise_endpoint, json=params, headers=exercise_headers)
print(response.json())
