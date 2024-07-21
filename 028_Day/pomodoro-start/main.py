import tkinter
from math import floor


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global check_label_text, reps, timer
    window.after_cancel(timer)
    check_label_text = ""
    check_label["text"] = check_label_text
    timer_label.config(text="Timer", fg=GREEN)
    reps = 0
    canvas.itemconfig(timer_text,text="00:00")




# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps in [1, 3, 5, 7]:
        count_down(int(WORK_MIN * 60))
        timer_label["text"] = "Work"
        timer_label["fg"] = GREEN
    elif reps in [2,4,6]:
        count_down(int(SHORT_BREAK_MIN*60))
        timer_label["text"] = "Break"
        timer_label["fg"] = PINK
    elif reps == 8:
        count_down(int(LONG_BREAK_MIN*60))
        timer_label["text"] = "Break"
        timer_label['fg'] = RED

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_mins = floor(count / 60)
    count_secs = count % 60
    if count_mins < 10:
        count_mins = f"0{count_mins}"
    
    if count_secs < 10:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text,text=f"{count_mins}:{count_secs}")
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            global CHECK_MARK, check_label_text
            check_label_text += CHECK_MARK
            check_label["text"] = check_label_text




# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width = 200,height=224,bg=YELLOW,highlightthickness=0)
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112,image=img)

timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

start_button = tkinter.Button(text="Start",bg=YELLOW, highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = tkinter.Button(text = "Reset",bg=YELLOW, highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

timer_label = tkinter.Label(text="Timer",fg=GREEN,font=(FONT_NAME,40,'bold'),bg=YELLOW)
timer_label.grid(column=1,row=0)

CHECK_MARK = "✓"
check_label_text = ""
check_label = tkinter.Label(fg = GREEN,font=(FONT_NAME, 30, 'bold'),bg=YELLOW)
check_label.grid(column=1,row=3)

window.mainloop()