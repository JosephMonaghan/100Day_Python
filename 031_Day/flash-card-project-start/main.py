from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME="Ariel"
FRONT_LANG = "French"
BACK_LANG = "English"


##Get Data
try:
    data = pandas.read_csv(filepath_or_buffer="./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(filepath_or_buffer="./data/french_words.csv")

data_dict={}
for row,val in data.iterrows():
    data_dict[val.French]=val.English

cards_complete = False

def new_word():
    global active_word, flipper,cards_complete
    try: 
        window.after_cancel(flipper)
    except:
        pass
    canvas.itemconfig(active_card,image=card_front)
    canvas.itemconfig(title_txt,text=FRONT_LANG,fill="black")
    if len(data_dict) > 0:
        active_word = random.choice(list(data_dict.items()))
        canvas.itemconfig(word_txt,text=active_word[0],fill="black")
        flipper = window.after(3000,flip_card)
    else:
        canvas.itemconfig(word_txt,text="All words completed!",fill="black")
        window.after_cancel(flipper)
        cards_complete = True 

def write_learned_names():
    global data_dict
    write_data = pandas.DataFrame.from_dict(data_dict.items())
    write_data.to_csv("./data/words_to_learn.csv",header=["French", "English"],index=False)


def flip_card():
    canvas.itemconfig(active_card,image=card_back)
    canvas.itemconfig(title_txt,text=BACK_LANG,fill="white")
    canvas.itemconfig(word_txt,text=active_word[1],fill="white")

def right():
    global active_word, cards_complete
    if cards_complete == False:
        data_dict.pop(active_word[0])
        write_learned_names()
        new_word()

def wrong():
    new_word()


##UI
window = Tk()
window.title("FlashCards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

active_card = canvas.create_image(400, int(526/2),image=card_front)
title_txt = canvas.create_text(400,150,font=(FONT_NAME,40,'italic'),text="French")
word_txt = canvas.create_text(400,263,font=(FONT_NAME,60,'bold'),text="Word")
new_word()
canvas.grid(column=0,row=0,columnspan=2)

#Buttons
correct_image = PhotoImage(file="./images/right.png")
correct_button = Button(command=right,image=correct_image,highlightthickness=0,bg=BACKGROUND_COLOR)
correct_button.grid(column=1,row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(command=wrong,image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR)
wrong_button.grid(column=0,row=1)




window.mainloop()
