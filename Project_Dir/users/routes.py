from flask import Blueprint, render_template, flash, redirect, url_for
from Project_Dir.users.forms import RegistrationForm, LoginForm

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Flash Message
        flash(f"Account successfully created for {form.username.data}!", "success")
        # Redirect Home
        return redirect(url_for("main.home"))
    return render_template("register.html", form=form)

@users.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)
