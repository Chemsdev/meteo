import streamlit as st
import requests, json


# Fonction permettent d'avoir la météo.
def found_temperature():
    temperature = 5
    humidity = 6
    pressure = 9
    report = 8
    return temperature, humidity, pressure, report


# Fonction permettent de mettre un background.
def background_front(url:str):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({url});
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
