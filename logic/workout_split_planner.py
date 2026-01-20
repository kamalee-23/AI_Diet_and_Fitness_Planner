def generate_weekly_plan(bmi_cat, goal, focus, free_time):

    # -------- SAFETY WARNINGS --------
    warning = None
    if bmi_cat in ["Overweight", "Obese"] and goal == "Weight Gain":
        warning = "⚠️ You are overweight. Weight gain is not recommended."
        goal = "Maintain"

    if bmi_cat == "Underweight" and goal == "Weight Loss":
        warning = "⚠️ You are underweight. Weight loss is unsafe."
        goal = "Maintain"

    # -------- BASE SETS / REPS --------
    if goal == "Weight Loss":
        sets = 4
        reps = 18
        rest = "30 sec"

    elif goal == "Weight Gain":
        sets = 5
        reps = 8
        rest = "75 sec"

    else:
        sets = 3
        reps = 12
        rest = "45 sec"

    # -------- FREE TIME ADJUSTMENT --------
    if free_time < 30:
        sets = max(2, sets - 1)

    elif free_time > 60:
        sets = min(6, sets + 1)
        if goal != "Weight Gain":
            reps = min(20, reps + 2)

    # -------- FOCUS AREA EXERCISES --------
    focus_exercises = {
        "Arms": ["Push-ups", "Tricep Dips", "Arm Circles"],
        "Legs": ["Squats", "Lunges", "Calf Raises"],
        "Lower Body": ["Squats", "Glute Bridge", "Step-ups"],
        "Upper Body": ["Push-ups", "Plank", "Shoulder Taps"],
        "Full Body": ["Jumping Jacks", "Squats", "Push-ups"]
    }

    support = ["Jumping Jacks", "Mountain Climbers"]

    weekly_plan = {
        "Day 1": focus_exercises[focus],
        "Day 2": support,
        "Day 3": focus_exercises[focus],
        "Day 4": ["Active Rest"],
        "Day 5": focus_exercises[focus],
        "Day 6": support,
        "Day 7": ["Rest"]
    }

    return weekly_plan, sets, reps, rest, warning
