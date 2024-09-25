#Peliä varten täytyy asentaa mysql-connector-python 8.0.29!!!

#Yhteyden luonti tietokantaan erillisessä filessä
#database.py kysyy tietokanta käyttäjän ja salasanan
import database
import kyselyt
from aliohjelmat_jesse_aleksanteri import pack1

#Importataan tähän eri aliohjelmat ja kyselyaliohjelmat yms
#Liimaillaan parhaamme mukaan ja tsemppiä :)


#"Yleiset arvot"
#Määritetään vakio komennot monikkoon
commands = ("vihje", "kohteet", "matkusta", "radio", "help")
#Matkalaukun sijaintai, mikä pitää arpoa
case_location = "EFHK"
#Main gameloop

#Kysytään käyttäjän input funktiolla
user_command = pack1.user_command(commands)

##Vihje funktio,  joka tulostaa maan vihjeen perustuen matkalaukun ICAO sijaintiin (case_location)
if user_command == commands[0]:  #VIHJE
    clue = database.database_query(
        kyselyt.query_country_hint(case_location)
    )
    pack1.country_clue(clue)

#Kohteet funktio,  kohteiden näyttäminen käyttäjälle (tällä hetkellä pelkät maat)
elif user_command == commands[1]: #KOHTEET
    countries = database.database_query(kyselyt.query_countries)
    pack1.user_search(countries)

