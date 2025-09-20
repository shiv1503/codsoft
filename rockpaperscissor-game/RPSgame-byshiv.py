# Rock Paper Scissors Game - by Shiv
# A simple game with a GUI using Tkinter

import tkinter as tk
import random

# Possible moves
moves = ['Rock', 'Paper', 'Scissors']

# Score counters
player_points = 0
computer_points = 0

# Function to play a round
def play_round(player_choice):
    """
    Handles the game logic each time the player clicks a button.
    """
    global player_points, computer_points

    # Random computer choice
    comp_choice = random.choice(moves)
    comp_choice_label.config(text=f"Computer picked: {comp_choice}")

    # Decide outcome
    if player_choice == comp_choice:
        result_text = "It's a Draw!"
    elif (
        (player_choice == 'Rock' and comp_choice == 'Scissors') or
        (player_choice == 'Scissors' and comp_choice == 'Paper') or
        (player_choice == 'Paper' and comp_choice == 'Rock')
    ):
        result_text = "🎉 You Won this Round!"
        player_points += 1
    else:
        result_text = "😢 Computer Won this Round!"
        computer_points += 1

    result_label.config(text=result_text)
    score_label.config(text=f"Score ➡ You: {player_points} | Computer: {computer_points}")

# Function to reset the scores
def reset_game():
    """
    Resets the scores and labels.
    """
    global player_points, computer_points
    player_points = 0
    computer_points = 0
    comp_choice_label.config(text="Computer picked: -")
    result_label.config(text="")
    score_label.config(text="Score ➡ You: 0 | Computer: 0")

# GUI Setup
window = tk.Tk()
window.title("Rock-Paper-Scissors Game - Shiv")
window.geometry("360x320")
window.configure(bg="#6ad9f8")
window.resizable(False, False)

# Heading label
tk.Label(window, text="Rock - Paper - Scissors", font=("Arial", 15, "bold")).pack(pady=5)
tk.Label(window, text="Pick your move below", font=("Arial", 12)).pack(pady=2)

# Frame for buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Buttons for moves
tk.Button(button_frame, text="Rock", width=10, command=lambda: play_round('Rock')).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play_round('Paper')).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play_round('Scissors')).grid(row=0, column=2, padx=5)

# Label to show computer's choice
comp_choice_label = tk.Label(window, text="Computer picked: -", font=("Arial", 12))
comp_choice_label.pack(pady=10)

# Label for result
result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Label for score
score_label = tk.Label(window, text="Score ➡ You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Reset button
tk.Button(window, text="Reset Game", width=15, command=reset_game).pack(pady=10)

# Run the app
window.mainloop()
