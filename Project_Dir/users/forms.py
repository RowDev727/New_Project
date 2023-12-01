from flask_wtf import FlaskForm
from flask import flash
from Project_Dir.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=26)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up!")
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            flash('username test')
            raise ValidationError('This username is already taken!')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            flash('email test')
            raise ValidationError('This email is already taken!')
    
    
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
    