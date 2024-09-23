#Peliä varten täytyy asentaa mysql-connector-python 8.0.29!!!

#Yhteyden luonti tietokantaan erillisessä filessä
#database.py kysyy tietokanta käyttäjän ja salasanan
import database
import kyselyt
#Importataan tähän eri aliohjelmat ja kyselyaliohjelmat yms
#Liimaillaan parhaamme mukaan ja tsemppiä :)



#Esimerkki miten kyselyt toteutetaan hyvällä tavalla?
print(database.database_query(kyselyt.sql_query_airport_name))

#Emme tarvitse kuin 1 funktion ja parametrina on sql kysely toisessa filessä
print(database.database_query(kyselyt.sql_query_airport_elevation))

#Main gameloop
