import streamlit as st
from model import train_model
from chatbot import get_chatbot_response

st.set_page_config(page_title="Fitness AI Planner", layout="wide")

st.title("💪 Personalized Workout & Diet Planner with AI")

# ----------------------------
# TRAIN MODEL
# ----------------------------
model, le_gender, le_goal, le_diet, le_activity, le_bmi_category = train_model()

# ----------------------------
# USER INPUT
# ----------------------------
st.sidebar.header("Enter Your Details")

age = st.sidebar.slider("Age", 15, 60, 22)

height = st.sidebar.number_input(
    "Height (cm)",
    min_value=120.0,
    max_value=220.0,
    value=165.0,
    step=0.5
)

# ✅ FIXED: Now allows weight below 40
weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=10.0,
    max_value=200.0,
    value=60.0,
    step=0.5
)

# Dynamic dropdowns (prevents unseen label errors)
gender = st.sidebar.selectbox("Gender", list(le_gender.classes_))
diet = st.sidebar.selectbox("Diet Type", list(le_diet.classes_))
activity = st.sidebar.selectbox("Activity Level", list(le_activity.classes_))

budget = st.sidebar.number_input(
    "Monthly Budget",
    min_value=1000,
    max_value=50000,
    value=5000,
    step=500
)

# ----------------------------
# BMI CALCULATION
# ----------------------------
bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    bmi_category = "Underweight"
elif bmi < 25:
    bmi_category = "Normal"
elif bmi < 30:
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

st.subheader("📊 BMI Result")
st.write("BMI:", round(bmi, 2))
st.write("BMI Category:", bmi_category)

# ----------------------------
# SAFE ENCODING FUNCTION
# ----------------------------
def safe_transform(encoder, value):
    if value in encoder.classes_:
        return encoder.transform([value])[0]
    else:
        return encoder.transform([encoder.classes_[0]])[0]

# Encode Inputs safely
gender_encoded = safe_transform(le_gender, gender)
diet_encoded = safe_transform(le_diet, diet)
activity_encoded = safe_transform(le_activity, activity)
bmi_category_encoded = safe_transform(le_bmi_category, bmi_category)

# ----------------------------
# PREDICTION
# ----------------------------
prediction = model.predict([[
    age,
    height,
    weight,
    gender_encoded,
    diet_encoded,
    activity_encoded,
    budget,
    bmi,
    bmi_category_encoded
]])

predicted_goal = le_goal.inverse_transform(prediction)[0]

st.subheader("🤖 AI Predicted Fitness Goal")
st.success(predicted_goal)

# ----------------------------
# WORKOUT PLAN
# ----------------------------
st.subheader("🏋️ Workout Plan")

if predicted_goal == "Weight Loss":
    st.write("• Running")
    st.write("• Jump Rope")
    st.write("• Squats")
    st.write("• Plank")

elif predicted_goal == "Muscle Gain":
    st.write("• Push-ups")
    st.write("• Bench Press")
    st.write("• Deadlift")
    st.write("• High Protein Diet")

else:
    st.write("• Walking")
    st.write("• Yoga")
    st.write("• Light Strength Training")

# ----------------------------
# DIET PLAN
# ----------------------------
st.subheader("🥗 Diet Plan")

if diet == "Vegetarian":
    st.write("• Paneer")
    st.write("• Dal")
    st.write("• Brown Rice")
    st.write("• Vegetables")

elif diet == "Non-Vegetarian":
    st.write("• Eggs")
    st.write("• Chicken")
    st.write("• Fish")
    st.write("• Rice")

elif diet == "Vegan":
    st.write("• Tofu")
    st.write("• Nuts")
    st.write("• Seeds")
    st.write("• Fruits")

# ----------------------------
# CHATBOT
# ----------------------------
st.subheader("💬 Fitness Chatbot")

query = st.text_input("Ask a fitness question:")

if query:
    response = get_chatbot_response(query)
    st.info(response)

st.success("Stay Consistent 💪 Fitness is a Journey 🚀")