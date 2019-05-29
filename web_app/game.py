# adapted from: https://github.com/prof-rossetti/rock-paper-scissors-py/blob/master/app/game.py



import random

GUI_WINDOW_TITLE = "Rock-Paper-Scissors"
WELCOME_MESSAGE = "Hi. Welcome to my Rock-Paper-Scissors game!"
GUI_PROMPT_MESSAGE = "Please choose an option from the dropdown:"

WIN_MESSAGE = "Congratulations, you won!"
LOSE_MESSAGE = "Oh, the computer won. It's ok."
TIE_MESSAGE = "Oh, it's a tie."

def random_choice(options=["rock", "paper", "scissors"]):
    return random.choice(options)

def determine_winner(choice1, choice2):
    """
    Determines the winning choice between two choices from selectable options: "rock", "paper", or "scissors".
    Returns the winning choice (e.g. "paper"), or None if there is a tie.
    Example: determine_winner("rock", "paper")
    """

    if choice1 == choice2:
        winner = None # the outcome is a tie
    else:
        choices = [choice1, choice2]
        choices.sort() # FYI: this is mutating

        if choices == ["paper", "rock"]:
            winner = "paper"
        elif choices == ["paper", "scissors"]:
            winner = "scissors"
        elif choices == ["rock", "scissors"]:
            winner = "rock"
        else:
            raise ValueError("OOPS, SOMETHING WENT WRONG")

    return winner
