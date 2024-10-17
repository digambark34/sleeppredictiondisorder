import pickle
import streamlit as st
import pandas as pd

# Load the trained model from the pickle file
with open('sleep_disorder_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to preprocess input data
def preprocess_input(gender, occupation, bmi_category):
    # Convert gender to binary: Male=1, Female=0
    gender_map = {'Male': 1, 'Female': 0}
    gender_encoded = gender_map[gender]

    # Convert occupation to numerical encoding
    occupation_map = {'Software Engineer': 0, 'Doctor': 1, 'Teacher': 2, 'Nurse': 3, 'Engineer': 4, 'Accountant': 5, 'Salesperson': 6}
    occupation_encoded = occupation_map[occupation]

    # Convert BMI category to numerical encoding
    bmi_map = {'Normal': 0, 'Overweight': 1, 'Obese': 2}
    bmi_encoded = bmi_map[bmi_category]

    return gender_encoded, occupation_encoded, bmi_encoded

# Create a Streamlit app
st.title('Sleep Disorder Prediction App')

# Create input fields for user data
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.number_input('Age', min_value=1, max_value=100)
occupation = st.selectbox('Occupation', ['Software Engineer', 'Doctor', 'Teacher', 'Nurse', 'Engineer', 'Accountant', 'Salesperson'])
sleep_duration = st.number_input('Sleep Duration (hours)', min_value=0, max_value=24)
quality_of_sleep = st.number_input('Quality of Sleep (1-10)', min_value=1, max_value=10)
physical_activity_level = st.number_input('Physical Activity Level (1-10)', min_value=1, max_value=10)
stress_level = st.number_input('Stress Level (1-10)', min_value=1, max_value=10)
heart_rate = st.number_input('Heart Rate (bpm)', min_value=40, max_value=200)
daily_steps = st.number_input('Daily Steps', min_value=0, max_value=50000)
bmi_category = st.selectbox('BMI Category', ['Normal', 'Overweight', 'Obese'])

# Create a button to predict sleep disorder
if st.button('Predict'):
    # Preprocess input data
    gender_encoded, occupation_encoded, bmi_encoded = preprocess_input(gender, occupation, bmi_category)

    # Create a Pandas DataFrame with the preprocessed user input
    input_data = pd.DataFrame({
        'Gender': [gender_encoded],
        'Age': [age],
        'Occupation': [occupation_encoded],
        'Sleep Duration': [sleep_duration],
        'Quality of Sleep': [quality_of_sleep],
        'Physical Activity Level': [physical_activity_level],
        'Stress Level': [stress_level],
        'Heart Rate': [heart_rate],
        'Daily Steps': [daily_steps],
        'BMI Category': [bmi_encoded]
    })

    # Make a prediction using the loaded model
    prediction = model.predict(input_data)

    # Display the prediction to the user
    st.write(f'Predicted Sleep Disorder: {prediction[0]}')
