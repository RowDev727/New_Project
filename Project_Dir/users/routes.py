from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from Project_Dir import db, bcrypt
from Project_Dir.models import User, Post
from Project_Dir.users.forms import RegistrationForm, LoginForm

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash Password submited to form
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        
        # Create User Object
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        # Submit Changes to DB
        db.session.add(user)
        db.session.commit()
            
        # Flash Message
        flash(f"Account successfully created for {form.username.data}!", "success")
        
        # Redirect Home
        return redirect(url_for("users.login"))
    return render_template("register.html", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Query user
        user = User.query.filter_by(username=form.username.data).first()
        
        # Check username:password combo
        if user and bcrypt.check_password_hash(user.password, form.password.data):        
            # If valid, login user and redirect home
            login_user(user, remember=form.remember.data)
            flash("Login Successful!", "info")
            return redirect(url_for("main.home"))
        else:
            # Flash message
            flash("Login unsuccessful.  Please check username/password", "danger")
    return render_template("login.html", form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
