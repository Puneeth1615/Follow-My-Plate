from datetime import datetime, timedelta

def suggest_meal_plan(current_meals, goal):
    suggestions_text = {
        'gain': 'To gain weight, focus on nutrient-dense foods: add healthy fats (avocados, nuts, olive oil), complex carbs (whole grains, sweet potatoes), and sufficient protein (lean meats, legumes, dairy). Consider an extra snack or larger portions.',
        'lose': 'To lose weight, prioritize lean proteins, abundant non-starchy vegetables, and moderate healthy fats. Reduce refined sugars, processed foods, and unhealthy fats. Focus on portion control and mindful eating.',
        'maintain': 'To maintain weight, aim for balanced meals with adequate protein, complex carbohydrates, and healthy fats. Focus on consistency with portion sizes and listen to your body\'s hunger cues.',
    }

    suggested_meals = {}
    for meal, description in current_meals.items():
        suggested_meals[meal] = f"Your {meal}: '{description}'. General advice for your goal: {suggestions_text[goal]}"

    return suggested_meals

def calculate_bmr(user):
    """
    Calculates Basal Metabolic Rate (BMR) using Mifflin-St Jeor Equation.
    Men: (10 * weight in kg) + (6.25 * height in cm) - (5 * age in years) + 5
    Women: (10 * weight in kg) + (6.25 * height in cm) - (5 * age in years) - 161
    """
    if not all([user.weight, user.height, user.age, user.gender]):
        return None

    weight_kg = user.weight
    height_cm = user.height
    age_years = user.age

    if user.gender == 'male':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) + 5
    elif user.gender == 'female':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) - 161
    else:
        return None

    return round(bmr)

def calculate_tdee(bmr, goal):
    """
    Estimates Total Daily Energy Expenditure (TDEE) based on BMR and a general activity level
    simplified for fitness goals. This is a very rough approximation.
    For a more accurate TDEE, a proper activity multiplier should be used.
    """
    if bmr is None:
        return None

    if goal == 'lose':
        return max(1200, bmr * 1.2 - 500)
    elif goal == 'gain':
        return bmr * 1.3 + 300
    elif goal == 'maintain':
        return bmr * 1.25
    else:
        return bmr * 1.2