
def recommend_diet(weight, height, goal):
    if goal == "Weight Loss":
        return {
            "Breakfast": "Oats + fruits + a protein source",
            "Lunch": "Brown rice/roti + vegetables + dal",
            "Dinner": "Vegetable soup + salad + protein",
            "Snacks": "Fruits, nuts, roasted chana",
            "Water": "3–4 liters",
            "Focus": "High-protein, high-fiber foods with controlled portions"
        }

    elif goal == "Weight Gain":
        return {
            "Breakfast": "Eggs/paneer + toast + banana",
            "Lunch": "Rice + dal + vegetables + curd",
            "Dinner": "Chapati + curry + protein source",
            "Snacks": "Banana, peanut butter, nuts, milk",
            "Water": "2.5–3 liters",
            "Focus": "Calorie-dense foods with adequate protein"
        }

    else:  # Maintain
        return {
            "Breakfast": "Balanced carbs + protein + fruits",
            "Lunch": "Rice/roti + vegetables + dal/protein",
            "Dinner": "Light protein-rich meal + vegetables",
            "Snacks": "Fruits, nuts, yogurt",
            "Water": "3 liters",
            "Focus": "Balanced nutrition and consistent portions"
        }
