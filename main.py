import streamlit as st
from utils import *
from cities import *
import folium
import os
from dotenv import load_dotenv


def main():

    load_dotenv()

    # Récupérer la clé API à partir des variables d'environnement
    api_key = os.getenv("api_key")

    background_front(url="https://medias.objectifgard.com/api/v1/images/view/6363e8dcb8e2787e72787ae6/article/image.jpg")
    st.title("WEATHER city France")

    # Input choix d'une ville.
    option_city = st.text_input("")

    # Bouton rechercher
    if st.button("rechercher"):

        # Lancement des résultats seulement si l'input est remplie.
        if not option_city == "":

            # Affichage des résultats seulement si la ville à été trouvée.
            try:

                # Affichage des résultats
                temperature, humidity, pressure, report = found_temperature(API_KEY=api_key, CITY=option_city)
                st.write(f"Temperature : {temperature}")
                st.write(f"Humidity :    {humidity}")
                st.write(f"Pressure :    {pressure}")
                st.write(f"Report :      {report}")
            except:

                # Message d'erreur si ville introuvable.
                st.error("Ville introuvable ou inexistante !")










main()
