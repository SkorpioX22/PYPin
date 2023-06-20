import random
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def guess_pin():
    user_pin = pin_entry.get()
    pin_guess = ""
    attempts = 0
    
    while pin_guess != user_pin:
        pin_guess = str(random.randint(0, 99)).zfill(2)
        guess_label.config(text="Final Guess: " + pin_guess)
        guess_label.update()
        attempts += 1

    messagebox.showinfo("Success", "PIN guessed successfully!\nNumber of attempts: " + str(attempts))

# Create the main window
window = tk.Tk()
window.title("PYPin V0.1.2")
window.geometry("300x200")

# Configure font
font = Font(family="Helvetica", size=16)

# Create and place the PIN entry field
pin_label = tk.Label(window, text="Enter your 2-digit PIN:", font=font)
pin_label.pack()
pin_entry = tk.Entry(window, show="*", font=font)
pin_entry.pack()

# Create and place the guess label
guess_label = tk.Label(window, text="Final Guess:", font=font)
guess_label.pack()

# Create and place the guess button
guess_button = tk.Button(window, text="Run Algorithm!", command=guess_pin, font=font)
guess_button.pack()

# Start the GUI event loop
window.mainloop()
