from question_model import Question
#from data import question_data
from quiz_brain import QuizBrain
import openTrivia_API_call
import os

os.system("Clear")

question_array = []
question_data = openTrivia_API_call.retrieve_questions()

for item in question_data:
    #question_array.append(Question(item["text"], item["answer"])) ##Old database
    question_array.append(Question(item["question"], item["correct_answer"])) #API call




quiz = QuizBrain(question_array)

score=0
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!")
print(f"Your final score was {quiz.score} / {quiz.question_number}")



