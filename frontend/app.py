import streamlit as st
import joblib

model = joblib.load("model.obj")
scaler = joblib.load("scaler.obj")

st.title("Rainfall Prediction")

input_boxes = {
    "pressure 9 am": st.number_input("Pressure Observed at 9 AM"),
    "wind gust speed": st.number_input("Wind Gust Speed"),
    "humidity 3 pm": st.number_input("Humidity Observed at 3 PM"),
    "Rainfall": st.number_input("Rainfall"),
    "Temperature 9 am": st.number_input("Temperature Observed at 9 AM"),
    "Minimum Temerature": st.number_input("Minimum Temerature"),
    "Cloud 3 pm": st.number_input("Clouds Observed at 3 PM")
}

if st.button("Predict"):

    data = list(input_boxes.values())
    prediction = model.predict([data])[0]

    if prediction == "No":
        st.write("## No Rainfall tomorrow")
    else:
        st.write("## Rainfall tomorrow")
