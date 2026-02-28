import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def train_model():

    data = pd.read_csv("fitness_dataset.csv")

    # Label Encoders
    le_gender = LabelEncoder()
    le_goal = LabelEncoder()
    le_diet = LabelEncoder()
    le_activity = LabelEncoder()
    le_bmi_category = LabelEncoder()

    # Encode categorical columns
    data["Gender"] = le_gender.fit_transform(data["Gender"])
    data["Fitness_Goal"] = le_goal.fit_transform(data["Fitness_Goal"])
    data["Diet_Type"] = le_diet.fit_transform(data["Diet_Type"])
    data["Activity_Level"] = le_activity.fit_transform(data["Activity_Level"])
    data["BMI_Category"] = le_bmi_category.fit_transform(data["BMI_Category"])

    # Features (X)
    X = data[[
        "Age",
        "Height_cm",
        "Weight_kg",
        "Gender",
        "Diet_Type",
        "Activity_Level",
        "Monthly_Budget",
        "BMI",
        "BMI_Category"
    ]]

    # Target (y)
    y = data["Fitness_Goal"]

    # Train Model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    return model, le_gender, le_goal, le_diet, le_activity, le_bmi_category