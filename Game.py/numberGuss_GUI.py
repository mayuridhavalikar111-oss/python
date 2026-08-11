import tkinter as tk
import random

# Create main window
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("400x400")

# Game variables
number = random.randint(1, 100)
attempts = 7

# Functions
def check_guess():
    global attempts
    
    try:
        guess = int(entry.get())
    except:
        result_label.config(text="Enter a valid number!")
        return
    
    if guess > number:
        result_label.config(text="Too High!")
    elif guess < number:
        result_label.config(text="Too Low!")
    else:
        result_label.config(text="🎉 Correct! You Win!")
        return
    
    attempts -= 1
    attempts_label.config(text=f"Attempts Left: {attempts}")
    
    if attempts == 0:
        result_label.config(text=f"😢 Game Over! Number was {number}")

def restart_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 7
    result_label.config(text="")
    attempts_label.config(text="Attempts Left: 7")
    entry.delete(0, tk.END)

# UI Elements
title = tk.Label(window, text="🎮 Guess the Number", font=("Arial", 18))
title.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

submit_btn = tk.Button(window, text="Submit Guess", command=check_guess)
submit_btn.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

attempts_label = tk.Label(window, text="Attempts Left: 7", font=("Arial", 12))
attempts_label.pack(pady=5)

restart_btn = tk.Button(window, text="Restart Game", command=restart_game)
restart_btn.pack(pady=10)

# Run the window
window.mainloop()