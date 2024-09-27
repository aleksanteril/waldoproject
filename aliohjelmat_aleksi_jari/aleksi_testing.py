# MATKUSTAMINEN (Heini)
# -> Kysy minne käyttäjä haluaa matkustaa
# -> Tee db query, joka tarkistaa, että syötetty maa on EU:ssa
# -> EI / KYLLÄ (iffi)
# Päivitä pelaajan location
# palauta paluu arvona mihin maahan matkustit


import mysql.connector
from geopy.distance import geodesic
import random

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='waldo_game',
         user='megapint',
         password='wine',
         autocommit=True
         )


def travel_to_next(next_destination):
    query = "SELECT name FROM country WHERE name = %s AND continent = 'EU'"

    kursori = yhteys.cursor()
    kursori.execute(query, (next_destination,))
    tulos = kursori.fetchone()

    if tulos:
        print(f"Matkustat maahan: {next_destination}")
    else:
        print(f"Maata {next_destination} ei löytynyt Euroopasta.")

    return next_destination


next_destination = input("Seuraava matkustuskohde?: ")
travel_to_next(next_destination)