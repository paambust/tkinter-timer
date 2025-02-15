from tkinter import *
import tkinter
from turtle import bgcolor, color
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER")
    check_label.config(text="")
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps +=1

    if reps % 8 == 0 :
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)

    else:
        count_down(work_sec)
        timer_label.config(text="Work Time")





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = (count % 60 )
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = windows.after(1000, count_down, count-1)
    else:
        start_timer()
        windows.lift()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range (work_sessions):
            marks += "✓"
        check_label.config(text= marks)

        




# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



timer_label=tkinter.Label(text="TIMER", font=("Arial", 30, "bold"), foreground="green", background=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=("Arial", 10, "bold"), highlightthickness=0, background=YELLOW, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", font=("Arial", 10, "bold"), highlightthickness=0, background=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=3)

check_label =tkinter.Label(font=("Arial", 10, "bold"), foreground="green", bg=YELLOW)
check_label.grid(column=1, row=3)




windows.mainloop()
