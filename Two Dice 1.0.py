from tkinter import *
import random

# Define some colors for the GUI
background_color = "#272727"
button_color = "#4287f5"
label_color = "#ffffff"

# Create the GUI
Windows10 = Tk()
Windows10.title("Two Dice")
Windows10.geometry("400x200")
Windows10.configure(bg=background_color)

# Initialize
rolls = 10000
avg_attempts = 0
sum_attempts = 0
S1 = 0
S = 0
r = True
avg_label = Label(
    Windows10,
    text="This software simulates rolling two dice,\n and calculates the average number of rolls needed to get a specific number on both dice.",
    bg=background_color,
    fg=label_color,
    font=("Helvetica", 7)
)
version = Label(Windows10, bg = background_color, fg=label_color, text="Version 1.0",font=("Helvetica", 7))
version.place(x = 1, y = 180)
def click():
    global r
    if start_button["text"] == "Start":
        avg_label.config(text="", font=("Helvetica", 15))
        start_button.config(text="Restart")

        roll_dice()
        r = True
    else:
        roll_dice()
        r = True
start_button = Button(Windows10, text="Start", bg=button_color, fg=label_color, font=("Helvetica", 16), command=click)
start_button.place(x=150, y=20, width=100, height=50)


def roll_dice():
    global avg_attempts, sum_attempts, r, rolls, S1, S
    sum_attempts = 0
    for i in range(rolls):
        L_1 = [1, 2, 3, 4, 5, 6]
        while(r == True):
            S += 1

            LRT = random.randint(0, 6), random.randint(0, 6)
            T1 = 1, 1
            if (LRT == T1):
                sum_attempts += S
                S = 0
                S1 += 1
            T2 = 2, 2
            if (LRT == T2):
                sum_attempts += S
                S = 0
                S1 += 1
            T3 = 3, 3
            if (LRT == T3):
                sum_attempts += S
                S = 0
                S1 += 1
            T4 = 4, 4
            if (LRT == T4):
                sum_attempts += S
                S = 0
                S1 += 1
            T5 = 5, 5
            if (LRT == T5):
                sum_attempts += S
                S = 0
                S1 += 1
            T6 = 6, 6
            if (LRT == T6):
                sum_attempts += S
                S = 0
                S1 += 1
            if(S1 == 10000):
                r = False
            if(r == False):
                S = 0
                S1 = 0
    avg_attempts = (sum_attempts / rolls)
    avg_label.config(text=f"Average attempts: {avg_attempts}")




# Initialize the label that will show the average number of attempts

avg_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Add an "Exit" button in the bottom right corner of the window
def exit_program():
    Windows10.destroy()
exit_button = Button(Windows10, text="X", bg="red", fg="white", font=("Helvetica", 16), command=exit_program)
exit_button.place(x=380, y=0, width=20, height=20)

Windows10.mainloop()
