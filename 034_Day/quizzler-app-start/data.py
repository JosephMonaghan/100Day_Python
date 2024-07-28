import requests

question_call = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
question_call.raise_for_status()

question_data = question_call.json()['results']
