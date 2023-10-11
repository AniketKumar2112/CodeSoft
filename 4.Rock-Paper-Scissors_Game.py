# Program to create a Rock-Paper-Scissors Game.

import tkinter as tk
import random

game_width = 400
game_hieght = 450

# Function to play a round of Rock-Paper-Scissors-

def play_round(user_choice):
    computer_choice = random.choice(choices)

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text=result_label.cget("text") + "\nIt's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_label.config(text=result_label.cget("text") + "\nYou win!")
    else:
        result_label.config(text=result_label.cget("text") + "\nComputer wins!")

# Function to reset the result label-

def reset_result_label():
    result_label.config(text="")

# To create the main window-

game = tk.Tk()
game.title("Rock-Paper-Scissors Game")
game.geometry(f"{game_width}x{game_hieght}")

# To define the choices-

choices = ["rock", "paper", "scissors"]

# To create a label for user instructions-

instructions_label = tk.Label(game, text="Choose Rock, Paper, or Scissors", width=30, font=10)
instructions_label.pack(pady=30)

# To create buttons for user's choices-

rock_button = tk.Button(game, text="Rock", command=lambda: play_round("rock"), width=30, font=10)
paper_button = tk.Button(game, text="Paper", command=lambda: play_round("paper"), width=30, font=10)
scissors_button = tk.Button(game, text="Scissors", command=lambda: play_round("scissors"), width=30, font=10)

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)

# To create a label to display the result-

result_label = tk.Label(game, text="", width=30, font=10)
result_label.pack(pady=15)

# To create a button to reset the result label-

reset_button = tk.Button(game, text="Play Again", command=reset_result_label, width=30, font=10)
reset_button.pack(pady=15)

# Main loop-

game.mainloop()
