from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, Length , NumberRange

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()]) #
    email = StringField('Email', validators=[DataRequired(), Email()]) #
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)]) #
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) #
    submit = SubmitField('Register') #


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()]) #
    password = PasswordField('Password', validators=[DataRequired()]) #
    submit = SubmitField('Login') #

class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, max=120)]) #
    height = IntegerField('Height (cm)', validators=[DataRequired(), NumberRange(min=50, max=250)]) #
    weight = IntegerField('Weight (kg)', validators=[DataRequired(), NumberRange(min=20, max=300)]) #
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()]) #
    goal = SelectField('Fitness Goal', choices=[ #
        ('gain', 'Gain Weight'), #
        ('lose', 'Lose Weight'), #
        ('maintain', 'Maintain Weight') #
    ], validators=[DataRequired()]) #

    diet = TextAreaField('Describe your current diet', validators=[DataRequired()]) #

    submit = SubmitField('Submit') #


class DietForm(FlaskForm):
    breakfast = TextAreaField('Breakfast', validators=[DataRequired()]) #
    lunch = TextAreaField('Lunch', validators=[DataRequired()]) #
    dinner = TextAreaField('Dinner', validators=[DataRequired()]) #
    snacks = TextAreaField('Snacks')
    submit = SubmitField('Get Suggestions') #

class FoodEntryForm(FlaskForm):
    description = StringField('Food Item/Description', validators=[DataRequired(), Length(max=255)])
    calories = FloatField('Calories (kcal)', validators=[DataRequired(), NumberRange(min=0.1)])
    meal_type = SelectField('Meal Type', choices=[
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    submit = SubmitField('Add Food Item')