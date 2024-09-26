#Peliä varten täytyy asentaa mysql-connector-python 8.0.29!!!

#Yhteyden luonti tietokantaan erillisessä filessä
#database.py kysyy tietokanta käyttäjän ja salasanan
import database
import kyselyt
from aliohjelmat_jesse_aleksanteri import pack1
from aliohjelmat_aleksi_jari import pack2

#Importataan tähän eri aliohjelmat ja kyselyaliohjelmat yms
#Liimaillaan parhaamme mukaan ja tsemppiä :)


#"Yleiset arvot"
#Määritetään vakio komennot monikkoon
commands = ("vihje", "kohteet", "matkusta", "radio", "help")




#Arvotaan matkalaukun maa, ja sen jälkeen arvotaan matkalaukun ICAO
case_country = pack2.case_randomizer(
    database.database_query(kyselyt.query_countries)
)
case_icao_location = pack2.case_randomizer(
    database.database_query(kyselyt.query_country_airports(case_country))
)

print("PRINT TAUSTATARINA TJPS")
# print("PRINT TARKOITUS esim. Löydä matkalaukku niin ja näin.")
# print("PRINT OHJEISTUS MITEN MATKUSTAA / SIIRTYY / komennot")
# print("PRINT KIRJOITA sana ICAO -> Kirjoita maan -> saat vastauksena sen pääkentän ICAO:n ")

#Pelin alustus, kysytään käyttäjän nimi ja syötetään se tietokantaan ID, LOCATION vakio 'EFHK'
username_exist = True
while username_exist:
    username = pack2.start_game()
    username_exist = database.database_query(kyselyt.query_check_username(username))
    if username_exist:
        print("Käyttäjänimi varattu")

#Pelin alustus, kysytään käyttäjän nimi ja syötetään se tietokantaan ID, LOCATION vakio 'EFHK'
database.database_update(kyselyt.query_new_username(username))

#Lasketaan alku sijainti, ja asetetaan se base etäisyydeksi kuuma kylmää varten
distance = database.database_query(kyselyt.query_distance_from_goal(case_icao_location, username))
#Laukun sijainti pelaajaan, monikossa indeksi 0
previous_distance_to_case = distance[0]


#Main gameloop
#Kysytään käyttäjän input funktiolla
user_command = pack1.user_command(commands)

##Vihje funktio,  joka tulostaa maan vihjeen perustuen matkalaukun ICAO sijaintiin (case_location)
if user_command == commands[0]:  #VIHJE
    clue = database.database_query(
        kyselyt.query_country_hint(case_icao_location)
    )
    pack1.country_clue(clue)

#Kohteet funktio,  kohteiden näyttäminen käyttäjälle (tällä hetkellä pelkät maat)
elif user_command == commands[1]: #KOHTEET
    countries = database.database_query(
        kyselyt.query_countries
    )
    pack1.user_search(countries)

#Matkustus tapahtumat, MAAN VALINTA, SITTEN KUUMA/KYLMÄ LASKENTA
elif user_command == commands[2]: #MATKUSTUS
    #matkustus() funktio database.database_query(kyselyt.query_countries)
    #Kuumakylmä laskenta välissä
    distance_goal_meters = database.database_query(
        kyselyt.query_distance_from_goal(case_icao_location, username)
    )
    pack1.hot_cold_mechanic(distance_goal_meters[0], previous_distance_to_case[0])

# radio komento signaalin vahvuuden
elif user_command == commands[3]: #RADIO
    pack1.signal_strength(database.database_query(kyselyt.query_distance_from_goal(case_icao_location, username)))



#Help komento, tulostetaan komennot
elif user_command == commands[4]:
    pack2.help() #Help-komento