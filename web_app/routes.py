
from flask import Blueprint, request, render_template

from game_utils.rock_paper_scissors import *

game_routes = Blueprint("game_routes", __name__)

#
# GET /
#
@game_routes.route("/")
def index():
    print("VISITING THE START PAGE")
    return render_template("start.html")

#
# GET /results
# GET /results?choice=rock
# POST /results
#
@game_routes.route("/results", methods=["GET", "POST"])
def results(choice=None):
    print("VISITING THE RESULTS PAGE")
    print("REQUEST PARAMS:", dict(request.args))
    print("REQUEST VALUES:", dict(request.values))

    options = ["rock", "paper", "scissors"]

    # CAPTURE INPUTS

    if "choice" in request.args:
        # HANDLE GET REQUEST WITH CHOICE IN URL PARAMS:
        user_choice = request.args["choice"]
    elif "choice" in request.values:
        # HANDLE POST REQUEST WITH CHOICE IN THE REQUEST BODY:
        user_choice = request.values["choice"]
    else:
        user_choice = "rock" # TODO flash and redirect back to start page

    if user_choice not in options:
        user_choice = "rock" # TODO flash and redirect back to start page
        #print("Expecting one of: 'rock', 'paper', or 'scissors' (lower case, without the quotation marks). Please try again.")

    print("You chose:", user_choice)

    # PROCESS INPUTS

    computer_choice = random_choice(options)
    print("The computer chose:", computer_choice)

    winning_choice = determine_winner(user_choice, computer_choice)

    if winning_choice:
        if winning_choice == user_choice:
            results_message = WIN_MESSAGE
        elif winning_choice == computer_choice:
            results_message = LOSE_MESSAGE
    else:
        results_message = TIE_MESSAGE

    print("RESULTS:", results_message)

    return render_template("results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        results_message=results_message
    )
