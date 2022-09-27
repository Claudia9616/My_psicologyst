import email
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')

class CreateUser(LoginForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Send')