def recommend_diet(weight, height, goal):
    if goal == "Weight Loss":
        return {
            "Breakfast": "Oats + fruits",
            "Lunch": "Brown rice + vegetables",
            "Dinner": "Salad + soup",
            "Snacks": "Fruits, nuts",
            "Water": "3–4 liters"
        }

    elif goal == "Weight Gain":
        return {
            "Breakfast": "Eggs / paneer + toast",
            "Lunch": "Rice + dal + vegetables",
            "Dinner": "Chapati + curry",
            "Snacks": "Banana, peanut butter",
            "Water": "2.5–3 liters"
        }

    else:  # Maintain
        return {
            "Breakfast": "Balanced carbs & protein",
            "Lunch": "Rice/roti + vegetables",
            "Dinner": "Light protein meal",
            "Snacks": "Fruits",
            "Water": "3 liters"
        }
