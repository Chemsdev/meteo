import streamlit as st
import requests, json


# Fonction permettent d'avoir la météo.
def found_temperature(API_KEY:str, CITY:str):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        return temperature, humidity, pressure, report[0]['description']
    else:
        print("error")
        
        
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
