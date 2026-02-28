def get_chatbot_response(user_input):

    user_input = user_input.lower()

    if "weight loss" in user_input:
        return "For weight loss, maintain calorie deficit and do cardio regularly."

    elif "muscle" in user_input:
        return "For muscle gain, increase protein intake and follow strength training."

    elif "diet" in user_input:
        return "Healthy diet includes protein, complex carbs and healthy fats."

    elif "bmi" in user_input:
        return "BMI = Weight(kg) / Height(m)^2"

    else:
        return "Ask about diet, workout, muscle gain, weight loss or BMI."