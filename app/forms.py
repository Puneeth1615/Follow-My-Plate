from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    height = IntegerField('Height (cm)', validators=[DataRequired()])
    weight = IntegerField('Weight (kg)', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    goal = SelectField('Goal', choices=[('gain', 'Gain Weight'), ('lose', 'Lose Weight'), ('maintain', 'Maintain Weight')], validators=[DataRequired()])
    submit = SubmitField('Save Profile')

class DietForm(FlaskForm):
    breakfast = TextAreaField('Breakfast', validators=[DataRequired()])
    lunch = TextAreaField('Lunch', validators=[DataRequired()])
    dinner = TextAreaField('Dinner', validators=[DataRequired()])
    submit = SubmitField('Get Suggestions')
