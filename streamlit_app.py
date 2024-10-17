import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Streamlit App Title
st.title("Student Performance Prediction")

# Introduction and instructions
st.write("""
### Instructions:
Please provide the required details below to predict the student's performance in Math Exam.
The model will predict whether the student is likely to pass or fail based on factors like gender, race, parental education level, etc.
""")

# Create form for user input
with st.form(key='predict_form'):
    
    # Gender input
    st.subheader("1. Gender")
    st.write("Select the gender of the student (Male/Female). Gender may have a subtle influence on academic performance.")
    gender = st.selectbox("Select Gender", ("Male", "Female"))

    # Race/Ethnicity input
    st.subheader("2. Race/Ethnicity")
    st.write("Select the race or ethnicity of the student. This data is used to identify potential disparities in academic performance across different ethnic groups.")
    race_ethnicity = st.selectbox("Select Race/Ethnicity", ("group A", "group B", "group C", "group D", "group E"))

    # Parental Level of Education input
    st.subheader("3. Parental Level of Education")
    st.write("Select the highest level of education attained by the student's parents. Parental education is often correlated with academic success.")
    parental_level_of_education = st.selectbox("Parental Level of Education", 
                                               ("Some high school", "High school", "Some college", "Associate's degree", "Bachelor's degree", "Master's degree"))

    # Lunch input
    st.subheader("4. Lunch")
    st.write("Select the type of lunch the student receives. Standard or free/reduced lunch is often linked to socioeconomic status, which can influence academic performance.")
    lunch = st.selectbox("Lunch Type", ("Standard", "Free/reduced"))

    # Test Preparation Course input
    st.subheader("5. Test Preparation Course")
    st.write("Choose whether the student has completed a test preparation course or not. Completing a preparation course may improve academic performance.")
    test_preparation_course = st.selectbox("Test Preparation Course", ("None", "Completed"))

    # Reading Score input
    st.subheader("6. Reading Score")
    st.write("Enter the student's reading score (0-100). This score is a direct measure of the student's reading ability and comprehension.")
    reading_score = st.number_input("Reading Score", min_value=0.0, max_value=100.0, step=0.1)

    # Writing Score input
    st.subheader("7. Writing Score")
    st.write("Enter the student's writing score (0-100). This score is a direct measure of the student's writing proficiency.")
    writing_score = st.number_input("Writing Score", min_value=0.0, max_value=100.0, step=0.1)

    # Submit button
    submit_button = st.form_submit_button(label='Predict')

# When form is submitted, run prediction
if submit_button:
    # Prepare data for prediction
    data = CustomData(
        gender=gender.lower(),
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education.lower(),
        lunch=lunch.lower(),
        test_preparation_course=test_preparation_course.lower(),
        reading_score=reading_score,
        writing_score=writing_score
    )
    
    # Convert to DataFrame
    pred_df = data.get_data_as_data_frame()

    # Predict performance
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    # Display prediction result
    st.write(f"### Predicted Result: **{results[0]}**")
    st.write("This prediction is based on the data you entered.")