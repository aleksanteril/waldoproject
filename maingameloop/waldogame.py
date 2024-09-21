#Peliä varten täytyy asentaa mysql-connector-python 8.0.29!!!

#Yhteyden luonti tietokantaan erillisessä filessä
#database.py kysyy tietokanta käyttäjän ja salasanan
import database


#Importataan tähän eri aliohjelmat ja kyselyaliohjelmat yms
#Liimaillaan parhaamme mukaan ja tsemppiä :)


#Esimerkki sql kysely! Esimerkin vuoksi miten kursori menee
sql = (f"SELECT name "
       f"FROM airport "
       f"WHERE iso_country = 'FI'")
kursori = database.yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
print(tulos)

#Main gameloop
