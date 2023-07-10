# import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

# All Flask, session and SQL settings below are based on CS50 Finance exercise

# Configure flask application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///doctor-calc.db")


def apology(message, code=400):
    # Render a message as an apology to a user.
    def escape(s):
        # Escape special characters.
        # https://github.com/jacebrowning/memegen#special-characters

        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    # Decorate routes to require login.
    # https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


@app.after_request
def after_request(response):
    # Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/centor-score")
def centorScore():
    return render_template("centor-score.html")


@app.route("/cha2ds2vasc-score")
def cha2ds2vascScore():
    return render_template("cha2ds2vasc-score.html")


@app.route('/favorite')
@login_required
# Add an item to favorites list
def favorite():
    # Get username and ID of currently logged in user
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]

    # Get the item that should be added to favorites
    favorite = request.args.get("type")

    # Insert a favorite into the database
    db.execute("INSERT INTO favorites (username, favorite) SELECT ?, ? WHERE NOT EXISTS (SELECT 1 FROM favorites WHERE username = ? AND favorite = ?)",
               username, favorite, username, favorite)

    # Redirect user to favorites
    return redirect("/favorites")


@app.route('/favorite-remove')
@login_required
# Remove an item from favorites list
def favoriteRemove():
    # Get username and ID of currently logged in user
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]

    # Get the item that should be removed from favorites
    favorite = request.args.get("type")

    # Remove data from the database where username and item match
    db.execute(
        "DELETE FROM favorites WHERE username = ? AND favorite = ?", username, favorite)

    # Redirect user to favorites
    return redirect("/favorites")


@app.route('/favorites')
@login_required
def favorites():

    # Get username of currently logged in user
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]

    # Query database for user favorites
    favorites = db.execute(
        "SELECT favorites.favorite, favorites_data.favorite_tag,favorites_data.favorite_name, favorites_data.favorite_link FROM favorites INNER JOIN favorites_data ON favorites.favorite=favorites_data.favorite_tag WHERE username = ? ORDER BY favorite_name", username)

    return render_template("favorites.html", favorites=favorites)


@app.route("/ibuprofen-dosage")
def ibuprofenDosage():
    return render_template("ibuprofen-dosage.html")


@app.route("/package-calculation")
def packageCalculation():
    return render_template("package-calculation.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Log a user in

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # Log a user out

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/paracetamol-dosage")
def paracetamolDosage():
    return render_template("paracetamol-dosage.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # Register a user

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username doesn't exist
        if len(rows) != 0:
            return apology("username already exists", 400)

        # Ensure username was submitted
        elif not request.form.get("username"):
            return apology("provide username", 400)

        # Ensure password and confirmation were submitted
        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("provide password and password confirmation", 400)

        # Ensure password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password confirmation doesn't match password", 400)

        # Insert username and hashed password to users
        username = request.form.get("username")
        password = request.form.get("password")
        hash = generate_password_hash(
            password, method='pbkdf2:sha256', salt_length=8)
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

        # Redirect user to home page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/wells-score-dvt")
def wellsScore():
    return render_template("wells-score-dvt.html")
