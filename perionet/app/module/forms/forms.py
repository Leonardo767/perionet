from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    nameLast = StringField('Last Name', validators=[
                           DataRequired(), Length(min=2, max=30)])
    nameFirst = StringField('First Name', validators=[
        DataRequired(), Length(min=2, max=30)])
    nameDob = StringField('DOB', validators=[], render_kw={
        "placeholder": "MM/DD/YYYY"})
    submit = SubmitField('Add Patient to Database')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
