import hmac
import os
from datetime import timedelta

import config
from flask import Flask, redirect, render_template, request, send_file, session, url_for


app = Flask(__name__, template_folder="tempates")
app.config.update(SECRET_KEY=config.SECRET_KEY)
app.permanent_session_lifetime = timedelta(days=365)


def allowed_login_email():
    return os.environ.get("LOGIN_EMAIL") or config.SMTP_USER


def valid_login(email, password):
    expected_email = allowed_login_email().strip().lower()
    expected_password = config.ADMIN_MASTER_PASSWORD

    return (
        expected_email
        and expected_password
        and hmac.compare_digest(email.strip().lower(), expected_email)
        and hmac.compare_digest(password, expected_password)
    )


@app.route("/")
def index():
    if session.get("user_email"):
        return redirect(url_for("home"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        if valid_login(email, password):
            session.permanent = True
            session["user_email"] = email.strip().lower()
            session["email_verified"] = False  # Место под будущую проверку кода из письма.
            return redirect(url_for("home"))

        error = "Неверная почта или пароль"

    return render_template("login.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    message = None

    if request.method == "POST":
        message = "Регистрация подготовлена. Отправку кода на почту подключим следующим шагом."

    return render_template(
        "register.html",
        message=message,
        smartcaptcha_sitekey=os.environ.get("SMARTCAPTCHA_SITEKEY", ""),
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/home")
def home():
    if not session.get("user_email"):
        return redirect(url_for("login"))
    return send_file("home.html")


@app.route("/api/people/active/all")
def active_people():
    if not session.get("user_email"):
        return {"error": "auth_required"}, 401
    return []


if __name__ == "__main__":
    app.run(debug=True)
