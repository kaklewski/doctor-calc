import os
import sys
import math

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
# from functools import wraps

# All Flask, session and SQL settings are based on CS50 Finance exercise

# Configure flask application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///doctorcalc.db")


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/centor-score")
def centorScore():
    return render_template("centor-score.html")


@app.route("/cha2ds2vasc-score")
def cha2ds2vascScore():
    return render_template("cha2ds2vasc-score.html")


@app.route("/ibuprofen-dosage", methods=["GET", "POST"])
def ibuprofenDosage():
    if request.method == "POST":

        if not request.form.get("age") or not request.form.get("weight"):
            return apology("not all values have been provided", 400)
        else:
            age = int(request.form.get("age"))
            weight = int(request.form.get("weight"))

            if age <= 12:
                maxDosage = str(30 * weight) + "mg"
            else:
                maxDosage = "1200mg"

            return render_template("ibuprofen-dosage.html", age=int(age), weight=int(weight), maxDosage=maxDosage)
    else:
        return render_template("ibuprofen-dosage.html")


@app.route("/package-calculation", methods=["GET", "POST"])
def packageCalculation():
    if request.method == "POST":

        if not request.form.get("intake") or not request.form.get("number-of-intakes") or not request.form.get("days") or not request.form.get("package-size"):
            return apology("not all values have been provided", 400)
        else:
            intake = float(request.form.get("intake"))
            numberOfIntakes = float(request.form.get("number-of-intakes"))
            days = float(request.form.get("days"))
            packageSize = float(request.form.get("package-size"))
            numberOfPackages = math.ceil(
                ((intake * numberOfIntakes * days) / packageSize))

        return render_template("package-calculation.html", intake=int(intake), numberOfIntakes=int(numberOfIntakes), days=int(days), packageSize=int(packageSize), numberOfPackages=int(numberOfPackages))

    else:
        return render_template("package-calculation.html")


@app.route("/paracetamol-dosage")
def paracetamolDosage():
    return render_template("paracetamol-dosage.html")


@app.route("/wells-score-dvt")
def wellsScore():
    return render_template("wells-score-dvt.html")
