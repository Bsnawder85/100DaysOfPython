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
reps = 0  # number of times the count_down() method is called.

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    # 8th and final rep
    if reps == 8:
        count_down(long_break_sec)
    # 1st / 3rd / 5th / 7th rep
    elif reps % 2 == 1:
        count_down(work_sec)
    # 2nd / 4th / 6th rep
    elif reps % 2 == 0:
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    # Below is where the timer will switch between working time and
    # break time once each count down reaches zero.
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)  # Canvas expects a PhotoImage data type
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
main_label = Label(text="Timer", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)
check_mark_label = Label(text="✔", fg=GREEN, bg=YELLOW)
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset")

main_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
check_mark_label.grid(row=3, column=1)



window.mainloop()
