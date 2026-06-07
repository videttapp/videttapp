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
    return render_template("verify.html")


@app.route("/verify-input", methods=["POST"])
def verify_input():
    input1 = request.form.get("input1")
    if input1 == "prexe":
        session["verified"] = 1
    return redirect("/")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )