class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.num_questions=len(self.question_list)

    def next_question(self):
        """Asks the user the next question, returns True/False depending on
        whether their answer is correct."""
        cur_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number}: {cur_question.text} True or False? ").title()
        self.check_answer(user_answer,cur_question.answer)

    def still_has_questions(self):
        """Checks if question number exceeds the total number of
        questions in the test bank. Returns True/False"""
        return self.question_number < self.num_questions
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("Nice, you got it right!")
        else:
            print("Oof, that's wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score} / {self.question_number}\n")
