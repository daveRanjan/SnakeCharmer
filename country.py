import requests
import random

def random_country():
    response = requests.get("https://restcountries.eu/rest/v2/all")
    random_country = response.json()[int(random.random() * 250)]
    return random_country
