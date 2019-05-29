
from flask import Blueprint, request, render_template

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
#
@game_routes.route("/results", methods=["GET", "POST"])
def hello(choice=None):
    print("VISITING THE RESULTS PAGE")
    print("REQUEST PARAMS:", dict(request.args))

    if "choice" in request.args:
        # HANDLE GET REQUEST WITH CHOICE IN URL PARAMS:
        choice = request.args["choice"]
    elif "choice" in request.values:
        # HANDLE POST REQUEST WITH CHOICE IN THE REQUEST BODY:
        choice = request.values["choice"]
    else:
        choice = "rock" # TODO flash and redirect back to start page

    return render_template("results.html", choice=choice)
