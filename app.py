import streamlit as st
from models.bmi_model import calculate_bmi, bmi_category
from logic.diet_planner import recommend_diet
from logic.workout_split_planner import generate_weekly_plan

# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="AI Diet and Fitness Planner",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 AI Diet and Fitness Planner")

# -------- INPUTS --------
height = st.number_input("Height (cm)", 100, 220)
weight = st.number_input("Weight (kg)", 30, 200)

goal = st.selectbox("Fitness Goal", ["Weight Loss", "Maintain", "Weight Gain"])
focus = st.selectbox(
    "Focus Area",
    ["Full Body", "Arms", "Legs", "Lower Body", "Upper Body"]
)
free_time = st.slider("Daily Free Time (minutes)", 10, 120, 30)

# -------- GENERATE --------
if st.button("Generate My Plan"):

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    st.success(f"BMI: {bmi} ({category})")

    # -------- BMI FEEDBACK --------
    if category == "Normal":
        st.success("You are in a healthy BMI range")
    elif category in ["Overweight", "Obese"]:
        st.warning("Focus on fat reduction and consistency")
    else:
        st.info("Gradual strength building recommended")

    # -------- PLAN SUMMARY --------
    st.markdown("### 📌 Your Plan Summary")
    st.write(f"""
    - **BMI Category:** {category}  
    - **Goal:** {goal}  
    - **Focus Area:** {focus}  
    - **Daily Time:** {free_time} minutes  
    """)

    st.markdown("---")

    # -------- DIET --------
    st.subheader("🍽 Diet Plan")
    diet = recommend_diet(weight, height, goal)
    for k, v in diet.items():
        st.write(f"**{k}:** {v}")

    # -------- WORKOUT --------
    st.subheader("🏋️ Weekly Workout Plan")

    plan, sets, reps, rest, warning = generate_weekly_plan(
        category, goal, focus, free_time
    )

    if warning:
        st.warning(warning)

    for day, exercises in plan.items():
        st.write(f"**{day}**")
        for e in exercises:
            if e in ["Rest", "Active Rest"]:
                st.write("  - Rest & recovery")
            else:
                st.write(f"  - {e}: {sets} sets × {reps} reps (Rest {rest})")

    # -------- WHY --------
    st.subheader("🤖 Why This Plan?")
    st.write("- Based on BMI")
    st.write("- Based on fitness goal")
    st.write("- Based on focus area")
    st.write("- Based on available time")

st.caption("⚠️ Educational purpose only. Consult a professional if needed.")
