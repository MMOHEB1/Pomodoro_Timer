from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel()
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(long_break)
        label = Label(text="NOICE! TAKE A 20 MIN BREAK", font=(FONT_NAME, 35, "bold"), fg=RED, highlightthickness=0,
                      bg=YELLOW)
        label.grid(column=1, row=0)
    elif REPS % 2:
        count_down(short_break)
        label = Label(text="YOU DESERVE 5 MINS!", font=(FONT_NAME, 35, "bold"), fg=PINK, highlightthickness=0,
                      bg=YELLOW)
        label.grid(column=1, row=0)
    else:
        count_down(work_sec)
        label = Label(text="GET TO WORKING", font=(FONT_NAME, 35, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
        label.grid(column=1, row=0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="POMODORO TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img_file = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img_file)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, bd=0, command=start_timer)
start_btn.grid(column=0, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

reset_btn = Button(text="Reset", highlightthickness=0, bd=0)
reset_btn.grid(column=2, row=2)

window.mainloop()
