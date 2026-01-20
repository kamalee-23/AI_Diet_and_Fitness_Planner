def recommend_workout(weight, height, goal, free_time):
    workout = []

    if goal == "Weight Loss":
        workout.append(("Jumping Jacks", 3, 20, "30 sec"))
        workout.append(("Squats", 3, 15, "30 sec"))
        workout.append(("Plank", 3, "30 sec", "30 sec"))

    elif goal == "Weight Gain":
        workout.append(("Push-ups", 4, 12, "60 sec"))
        workout.append(("Squats", 4, 10, "60 sec"))
        workout.append(("Lunges", 3, 12, "60 sec"))

    else:
        workout.append(("Push-ups", 3, 12, "45 sec"))
        workout.append(("Squats", 3, 12, "45 sec"))
        workout.append(("Plank", 3, "30 sec", "45 sec"))

    return workout
