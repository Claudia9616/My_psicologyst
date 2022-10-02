from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')

class CreateUser(LoginForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    id_number = IntegerField('Id number', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', choices=['Male', 'Female', 'Other'], validators=[DataRequired()])
    submit = SubmitField('Send')

class SuccessStory(FlaskForm):
    score = SelectField(
        'Satisfaction level', 
        choices=['Good', 'Medium', 'Bad'], 
        validators=[DataRequired()]
    )
    story = StringField(
        "Success story", 
        validators=[DataRequired(), Length(min=10, max=250)]
    )
    recommendation = SelectField(
        'Do you recommend the platform?', 
        choices=['Yes', 'No'], 
        validators=[DataRequired()]
    )
    submit = SubmitField('Send')