import json
import requests

def retrieve_questions():
    """Retrieves 10 True/False questions from OpenTrivia.com and returns a data file similar to data.py"""
    url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean"
    api_result = requests.get(url)
    if api_result.status_code == 200:
        content = json.loads(api_result.content.decode('utf-8'))
        question_database=[]
        for question_num in range(len(content["results"])):
            question_database.append(content["results"][question_num])
        return question_database
        
    else:
        print(f"API call failed with code: {api_result.status_code}")
        return


