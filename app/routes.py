from flask import render_template, redirect, url_for, flash, request, jsonify
from app import app, db
from app.forms import RegistrationForm, LoginForm, ProfileForm, DietForm, FoodEntryForm
from app.models import User, FoodEntry
from flask_login import login_user, logout_user, login_required, current_user
from app.diet_logic import suggest_meal_plan, calculate_bmr, calculate_tdee
from datetime import datetime, timedelta

# New Home Page Route
@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('home.html') # Render the new home.html

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
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            if not user.age or not user.height or not user.weight:
                flash('Please complete your profile to use the dashboard.', 'info')
                return redirect(url_for('profile'))
            return redirect(url_for('dashboard'))
        flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home')) # Redirect to home page after logout

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.age = form.age.data
        current_user.height = form.height.data
        current_user.weight = form.weight.data
        current_user.gender = form.gender.data
        current_user.goal = form.goal.data
        current_user.diet = form.diet.data
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('profile.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if not current_user.age or not current_user.height or not current_user.weight or not current_user.gender or not current_user.goal:
        flash('Please complete your profile first to access the dashboard.', 'warning')
        return redirect(url_for('profile'))

    bmr = calculate_bmr(current_user)
    daily_calories_target = calculate_tdee(bmr, current_user.goal) if bmr else 0

    today = datetime.utcnow().date()
    today_entries = FoodEntry.query.filter_by(author=current_user).filter(
        db.func.date(FoodEntry.date_posted) == today
    ).order_by(FoodEntry.date_posted.asc()).all()

    calories_consumed_today = sum(entry.calories for entry in today_entries)
    calories_remaining_today = daily_calories_target - calories_consumed_today

    food_entry_form = FoodEntryForm()
    if food_entry_form.validate_on_submit() and food_entry_form.submit.data:
        new_entry = FoodEntry(
            description=food_entry_form.description.data,
            calories=food_entry_form.calories.data,
            meal_type=food_entry_form.meal_type.data,
            author=current_user
        )
        db.session.add(new_entry)
        db.session.commit()
        flash('Food item added successfully!', 'success')
        return redirect(url_for('dashboard'))

    weekly_labels = []
    weekly_data = []
    start_of_week = today - timedelta(days=6)

    for i in range(7):
        current_date = start_of_week + timedelta(days=i)
        weekly_labels.append(current_date.strftime('%a, %b %d'))

        daily_calories_sum = db.session.query(db.func.sum(FoodEntry.calories)).filter_by(
            user_id=current_user.id
        ).filter(
            db.func.date(FoodEntry.date_posted) == current_date
        ).scalar() or 0
        weekly_data.append(round(daily_calories_sum, 2))

    meal_suggestion_form = DietForm()
    suggested_meal_plan_result = None
    if meal_suggestion_form.validate_on_submit() and meal_suggestion_form.submit.data:
        current_meals_input = {
            'breakfast': meal_suggestion_form.breakfast.data,
            'lunch': meal_suggestion_form.lunch.data,
            'dinner': meal_suggestion_form.dinner.data,
            'snacks': meal_suggestion_form.snacks.data
        }
        suggested_meal_plan_result = suggest_meal_plan(current_meals_input, current_user.goal)

    return render_template(
        'dashboard.html',
        user=current_user,
        daily_calories=daily_calories_target,
        calories_consumed=calories_consumed_today,
        calories_remaining=calories_remaining_today,
        food_entry_form=food_entry_form,
        today_entries=today_entries,
        weekly_labels=weekly_labels,
        weekly_data=weekly_data,
        meal_suggestion_form=meal_suggestion_form,
        suggested_meal_plan_result=suggested_meal_plan_result
    )

@app.route('/delete_food_entry/<int:entry_id>', methods=['POST'])
@login_required
def delete_food_entry(entry_id):
    entry = FoodEntry.query.get_or_404(entry_id)
    if entry.user_id != current_user.id:
        flash('You are not authorized to delete this entry.', 'danger')
        return redirect(url_for('dashboard'))

    db.session.delete(entry)
    db.session.commit()
    flash('Food entry deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    return redirect(url_for('profile'))