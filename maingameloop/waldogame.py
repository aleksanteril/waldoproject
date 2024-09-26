#Peliä varten täytyy asentaa mysql-connector-python 8.0.29!!!

#Yhteyden luonti tietokantaan erillisessä filessä
#database.py kysyy tietokanta käyttäjän ja salasanan
import database
import kyselyt
from aliohjelmat_jesse_aleksanteri import pack1
from aliohjelmat_aleksi_jari import pack2
from aliohjelmat_jesse_aleksanteri.pack1 import signal_strength

#Importataan tähän eri aliohjelmat ja kyselyaliohjelmat yms
#Liimaillaan parhaamme mukaan ja tsemppiä :)


#"Yleiset arvot"
#Määritetään vakio komennot monikkoon
commands = ("clue", "destinations", "travel", "radio", "help", "exit")
#case_country, case_icao_location, username, user_command


#Lista pelin maista joihin helppo verrata, listassa on eroteltu suomi pois 'lähtömaa'
countries_list = []
for country in database.database_query(kyselyt.query_countries):
    if country[0] != 'Finland':
        countries_list.append(country[0].lower())



print("\n")
print('''You've arrived at Helsinki-Vantaa airport, where you meet your good friend Waldo.

Waldo is a world-famous adventurer known for his red & white striped shirt and blue hat. 
He has travelled all over the world, but his valuable suitcase mysteriously disappeared. 
The suitcase contained Waldo's most important discoveries and notes, but fortunately, Waldo has installed a radio-transmitter in it.

Now Waldo needs your help to find his suitcase. Together, you set off around the world, using the radio-transmitter in the suitcase. 

Safe travels!''')

#Haluatko aloittaa pelin funktio
pack1.start_game()



#Arvotaan matkalaukun maa, ja sen jälkeen arvotaan matkalaukun ICAO
case_country = 'Finland'
while case_country == 'Finland':
    case_country = pack2.case_randomizer(
        database.database_query(kyselyt.query_countries)
    )
case_icao_location = pack2.case_randomizer(
    database.database_query(kyselyt.query_country_airports(case_country))
)
print(case_icao_location, case_country) #TÄMÄ ON DEVAUSTA VARTEN MUISTA KOMMENTOIDA POIS!

#Pelin alustus, kysytään käyttäjän nimi ja tarkistetaan onko se uniikki
print("\nWell let's get going!, says Waldo")
username_exist = True
while username_exist:
    username = pack2.input_username()
    username_exist = database.database_query(kyselyt.query_check_username(username))
    if username_exist:
        print("\nWaldo doesn't believe you!")

#Pelin alustus, kysytään käyttäjän nimi ja syötetään se tietokantaan ID, LOCATION vakio 'EFHK'
database.database_update(kyselyt.query_new_username(username))

#Lasketaan alkusijainti, ja asetetaan se base-etäisyydeksi kuuma/kylmää varten
distance = database.database_query(kyselyt.query_distance_from_goal(case_icao_location, username))
#Laukun sijainti pelaajaan, monikossa indeksi 0
previous_distance_to_case = distance[0]

user_command = None
while user_command != 'exit':
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
        pack1.user_search(countries_list)

    #Matkustus tapahtumat, MAAN VALINTA, SITTEN KUUMA/KYLMÄ LASKENTA
    elif user_command == commands[2]: #MATKUSTUS
        valid_country = False
        while not valid_country:
            travel_country = pack1.travel(countries_list)
            valid_country = database.database_check_query(kyselyt.query_check_country(travel_country))
        country_icaos = database.database_query(kyselyt.query_country_airports(travel_country))
        country_icao = country_icaos[0]

        #LOCATION PÄIVITTÄMINEN PELAAJALLE TIETOKANTAAN
        database.database_update(kyselyt.query_insert_location(country_icao[0], username))

        #KUUMA/KYLMÄ MEKANIIKKA
        distance_goal_meters = database.database_query(
            kyselyt.query_distance_from_goal(case_icao_location, username)
        )
        pack1.hot_cold_mechanic(distance_goal_meters[0], previous_distance_to_case[0])
        previous_distance_to_case = distance_goal_meters[0]

    #Radio komento signaalin vahvuuden tulostamiseen
    elif user_command == commands[3]: #RADIO
        pack1.signal_strength(
            database.database_query(kyselyt.query_distance_from_goal(case_icao_location, username))
        )

    #Help komento, tulostetaan help print
    elif user_command == commands[4]:
        pack2.help() #Help-komento