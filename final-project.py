import streamlit as st
import numpy as np

# Create a Streamlit web application
st.title("BMI Calculator")

# Create input controls
name = st.text_input("Enter your name")
gender = st.radio("Select your gender", ("Male", "Female", "Other"))
age = st.number_input("Enter your age", min_value=1, max_value=150, step=1)
address = st.text_area("Enter your address")
hobbies = st.write("Select your hobbies")
reading = st.checkbox("Reading")
writing = st.checkbox("Writing")
swimming = st.checkbox("Swimming")
travelling = st.checkbox("Travelling")
weight = st.number_input("Enter your weight in kg", min_value=0.0, max_value=500.0, step=0.1)
height = st.number_input("Enter your height in cm", min_value=0.0, max_value=300.0)

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = weight / np.square(height / 100)
    st.write(f"{name}, your BMI is {bmi:.2f}")
