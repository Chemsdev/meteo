import pytest
from main import found_temperature
from utils import cities
import streamlit as st 
api_key = "4ad672be71f6807bf029188203bcebaa"

# Test Functions found_temperature
@pytest.mark.parametrize(
    "key, city, expected",
    [
        (api_key, "Paris", (float, int, int, str)),
        (api_key, "Lyon",  (float, int, int, str)),
        (api_key, "Nice",  (float, int, int, str)),
    ],
)

# On test avec différents inputs les types des outputs.
def test_country(key, city, expected):
    result = found_temperature(API_KEY=key, CITY=city)
    assert isinstance(result, tuple)
    assert all(isinstance(value, expected_type) for value, expected_type in zip(result, expected))



# Tests avec différents output
@pytest.mark.parametrize(
    "option, cities_list, expected",
    [
        ("Paris",     [cities], True),
        ("Marseille", [cities], False),
        ("Nice",      [cities], True),
    ],
)

# Fonction pour vérifier si l'option saisie est dans la liste.
def check_input(option_city, cities):
    return option_city in cities

# Comparaison de l'input avec le résultat attendu.
def test_check_input(option, cities_list, expected):
    result = check_input(option, cities_list)
    assert result == expected
    
    