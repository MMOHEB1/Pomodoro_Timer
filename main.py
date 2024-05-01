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


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        count_down(work_sec)
        REPS += 1
    elif REPS == 2 or REPS == 4 or REPS == 6:
        count_down(short_break)
        REPS += 1
    elif REPS == 8:
        count_down(long_break)
        REPS = 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="POMODORO TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img_file = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img_file)
timer = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, bd=0, command=start_timer)
start_btn.grid(column=0, row=2)

tick_label = Label(text="✅", bg=YELLOW)
tick_label.grid(column=1, row=3)

reset_btn = Button(text="Reset", highlightthickness=0, bd=0)
reset_btn.grid(column=2, row=2)

window.mainloop()
