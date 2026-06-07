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
    dob = request.form.get("DOB")
    favorite_colleague = request.form.get("favorite-colleague")
    if dob[-5:] == "06-06":
        if favorite_colleague.lower().strip() in ["jacob", "jacob carter", "jacob c", "jake", "jakobski", "jacobski", "jacob william carter"]:
            session["verified"] = 1
            return redirect("/")
    else:
        return redirect("/verify?err=invalid")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )