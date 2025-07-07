def suggest_meals(breakfast, lunch, dinner, goal):
    suggestions = {
        'gain': 'Add nuts, avocados, and whole grains.',
        'lose': 'Use lean proteins, greens, and avoid sugar.',
        'maintain': 'Balance portions and eat moderate carbs and protein.'
    }

    return {
        'breakfast': f"{breakfast} → Suggestion: {suggestions[goal]}",
        'lunch': f"{lunch} → Suggestion: {suggestions[goal]}",
        'dinner': f"{dinner} → Suggestion: {suggestions[goal]}"
    }
