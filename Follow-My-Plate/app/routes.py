from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import RegistrationForm, LoginForm, ProfileForm, DietForm
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from app.diet_logic import suggest_meals
from app.forms import DietForm



@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('profile'))
        flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.age = form.age.data
        current_user.height = form.height.data
        current_user.weight = form.weight.data
        current_user.gender = form.gender.data
        current_user.goal = form.goal.data
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('profile.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if not current_user.age:
        flash('Please complete your profile first.', 'warning')
        return redirect(url_for('profile'))

    form = DietForm()
    result = None

    if form.validate_on_submit():
        current_meals = {
            'breakfast': form.breakfast.data,
            'lunch': form.lunch.data,
            'dinner': form.dinner.data,
            'snacks': form.snacks.data
        }

        result = suggest_meal_plan(current_meals, current_user.goal)

    return render_template(
        'dashboard.html',
        user=current_user,
        form=form,
        result=result
    )

