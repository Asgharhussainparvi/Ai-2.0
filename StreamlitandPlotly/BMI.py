import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px 
import time as t

st.title("BMI Calculator")

# Radio button for height unit selection
height_unit = st.radio("Select height unit:", ("Centimeters (cm)", "Feet (ft)", "Meter (m)"))

if height_unit == "Centimeters (cm)":
    height_cm = st.number_input("Enter your height in centimeters (cm)", min_value=1.0, max_value=170.0)
    height_meters = height_cm / 100  
elif height_unit == "Feet (ft)":
    height_ft = st.number_input("Enter your height in feet (ft)", min_value=1.0, max_value=7.0)  
    height_inches = st.number_input("Enter your height in inches (in)", min_value=1.0, max_value=12.0)  
    total_inches = (height_ft * 12) + height_inches
    height_meters = total_inches * 0.0254 
elif height_unit == "Meter (m)":
    height_meters = st.number_input("Enter your height in meters (m)", min_value=1.0, max_value= 5)

else:  
    height_meters = 0

weight = st.number_input("Enter your weight in kilograms (kg)", min_value=1.0, max_value=150.0)

# Calculate BMI 
if height_meters > 0:
    bmi = weight / (height_meters ** 2)
    st.write(f"Your BMI is: {bmi}")

    # Interpret BMI
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 25:
        st.write("You have a healthy weight.")
    elif 25 <= bmi < 30:
        st.write("You are overweight.")
    elif 30 <= bmi < 35:
        st.write("You are obese.")
    else:
        st.write("You are severely obese.")
else:
    st.write("Please enter a valid height.")
