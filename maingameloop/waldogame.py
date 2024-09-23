#Peliä varten täytyy asentaa mysql-connector-python 8.0.29!!!

#Yhteyden luonti tietokantaan erillisessä filessä
#database.py kysyy tietokanta käyttäjän ja salasanan
import database
import kyselyt
from aliohjelmat_jesse_aleksanteri import pack1
#Importataan tähän eri aliohjelmat ja kyselyaliohjelmat yms
#Liimaillaan parhaamme mukaan ja tsemppiä :)





case_location = "EGBN"
#Main gameloop
##Vihje funktio joka tulostaa maan vihjeen perustuen matkalaukun ICAO sijaintiin (case_location)

pack1.clue(database.database_query(kyselyt.query_country_hint(case_location)))

