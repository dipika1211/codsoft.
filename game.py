import random
import tkinter as tk
from tkinter import messagebox

# Function to play the game
def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Game logic to determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        global user_score
        user_score += 1
    else:
        result = "Computer wins!"
        global computer_score
        computer_score += 1

    # Display result and update score
    result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}.\n{result}")
    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")

# Function to reset the game for another round
def reset_game():
    result_label.config(text="")
    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")

# Create the main application window
window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x400")
window.configure(bg='black')  # Setting the background color to black

# Initialize scores
user_score = 0
computer_score = 0

# Title Label
title_label = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 16), fg="white", bg="black")
title_label.pack(pady=10)

# Game instructions label
instruction_label = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12), fg="white", bg="black")
instruction_label.pack(pady=5)

# Buttons for user to select Rock, Paper, or Scissors
rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"), font=("Arial", 12), bg="gray", fg="white")
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"), font=("Arial", 12), bg="gray", fg="white")
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"), font=("Arial", 12), bg="gray", fg="white")
scissors_button.pack(pady=5)

# Label to display the result of each round
result_label = tk.Label(window, text="", font=("Arial", 12), fg="green", bg="black")
result_label.pack(pady=10)

# Label to display the score
score_label = tk.Label(window, text=f"User: {user_score}  Computer: {computer_score}", font=("Arial", 12), fg="white", bg="black")
score_label.pack(pady=10)

# Play again button
play_again_button = tk.Button(window, text="Play Again", command=reset_game, font=("Arial", 12), bg="gray", fg="white")
play_again_button.pack(pady=5)

# Run the application
window.mainloop()
