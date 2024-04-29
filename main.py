from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    canvas.itemconfig(timer, text=count)
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
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_btn = Button(text="Start", highlightthickness=0, bd=0)
start_btn.grid(column=0, row=2)

tick_label = Label(text="✅", bg=YELLOW)
tick_label.grid(column=1, row=3)

reset_btn = Button(text="Reset", highlightthickness=0, bd=0)
reset_btn.grid(column=2, row=2)

window.mainloop()
