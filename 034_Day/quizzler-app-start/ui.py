from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"

from tkinter import *

class QuizInterface:
    def __init__(self,quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)

        #Create canvas and question text
        self.cv = Canvas(self.window,width=300,height=250,bg="white")
        self.cv_text = self.cv.create_text(150,125,text="Sample text",font=(FONT_NAME,20,'italic'),width=280)
        self.cv.grid(column=0,row=1,columnspan=2,pady=50)

        #Scoreboard
        self.score_label = Label(self.window,text="Score: 0",bg=THEME_COLOR,fg="white",padx=20,pady=20)
        self.score_label.grid(column=1,row=0)

        #Right/Wrong buttons
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")

        self.right_button = Button(self.window,
                                   image=self.true_img,
                                   bg=THEME_COLOR,
                                   highlightthickness=0,
                                   padx=20,
                                   pady=20,
                                   command=lambda:self.answered(answer="true"))
        self.right_button.grid(row=2,column=0)

        self.false_button = Button(self.window,
                                   image=self.false_img,
                                   bg=THEME_COLOR,
                                   highlightthickness=0,
                                   padx=20,
                                   pady=20,
                                   command=lambda: self.answered(answer="false"))
        self.false_button.grid(row=2,column=1)


        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.cv.itemconfig(self.cv_text,text=question)
        else:
            self.cv.itemconfig(self.cv_text,text="You've reached the end of the quiz!")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def answered(self,answer):
        correct = self.quiz.check_answer(user_answer=answer)
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if correct:
            self.cv.config(bg='green')
            self.window.update_idletasks()
            self.window.after(500)
            self.cv.config(bg='white')
            self.window.update_idletasks()
        else:
            self.cv.config(bg='red')
            self.window.update_idletasks()
            self.window.after(500)
            self.cv.config(bg="white")
            self.window.update_idletasks()
        
        self.get_next_question()
    
    def empty(self):
        pass
