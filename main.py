from flask import Flask, render_template, redirect, session, request
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = "jebrifbesbfirg783rt4398r2h"


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not session.get("verified"):
            return redirect("/verify")
        return func(*args, **kwargs)

    return decorated_view


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/verify")
def verify():
    err = "none"
    err = request.args.get("err")
    return render_template("verify.html", err=err)


@app.route("/verify-input", methods=["POST"])
def verify_input():
    dob = request.form.get("DOB", "")
    favorite_colleague = request.form.get("favorite-colleague", "")
    good_list = [
        "jacob",
        "jacob carter",
        "jacob c",
        "jake",
        "jakobski",
        "jacobski",
        "jacob william carter"
        "jacob1carter",
        "jwc",
        "jacob willian carter"
    ]
    bad_list = [
        "lara",
        "lara drew",
        "la la",
        "lauren",
        "lkd",
        "lovanoid",
        "drew",
        "will",
        "maj",
        "will majury"
        "willaim",
        "william majury"
        "william maj",
        "will jam",
        "william jam",
        "jam jam",
        "jammy will"
        "jam",
        "majury"
        "liam"
        "liam maj"
    ]
    
    if favorite_colleague.lower().strip() in bad_list:
        print("HERE")
        return redirect("/verify?err=traitor")
    elif favorite_colleague.lower().strip() in good_list:
        if dob[-5:] == "06-06":
            session["verified"] = 1
            return redirect("/")

    return redirect("/verify?err=invalid")


@app.route("/lock")
def lock():
    session.pop("verified", None)
    return redirect("/verify")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )