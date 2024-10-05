#Peliä varten täytyy asentaa mysql-connector-python 8.0.29!!!
#Peliä varten täytyy asentaa playsound, ja pyfiglet

#Yhteyden luonti tietokantaan erillisessä filessä
#Importataan kyselyt.py ja database.py ja random, audio ja animations
import database
import kyselyt
import random
import animations
import audio_library
import ascii_countries # lisätty clueta varte
from jokes import joket

#Importataan tähän eri aliohjelmat ja kyselyaliohjelmat yms
#Liimaillaan parhaamme mukaan ja tsemppiä :)

#ALIOHJELMAT LÖYTYVÄT TÄSTÄ

def clear_screen():
    print('\n' * 50)
    return


#Funktio jolla tarkastetaan onko pelaaja löytänyt matkalaukun maan
def goal_check(username):
    user_country = database.database_query_fetchone(kyselyt.query_fetch_user_country(username))
    case_country = database.database_query_fetchone(kyselyt.query_fetch_suitcase_country(username))
    if user_country[0] == case_country[0]:
        return True
    else:
        return False


# ottaa listan ja arpoo jonkun arvon listasta
def list_random(list):
    random_index = random.randint(0, len(list)-1)
    random_str = list[random_index]
    return random_str[0]


#Kilometrilaskuri laskee edellisen icaon ja uuden paikan välin kilometrit kyselyn avulla
def kilometer_counter(new_icao, previous_icao):
    meters_tuple = database.database_query_fetchone(kyselyt.query_distance_between_locations(new_icao,previous_icao))
    kilometers = meters_tuple[0] / 1000
    return kilometers


#tulostaa komennot käyttäjälle
def help():
    #print("\nUsing command 'help' opens this window.")
    print("\nUsing command 'clue' gives you a clue.")
    print("Using command 'destinations' prints the country's you can travel to.")
    print("Using command 'travel' travels you to your country of choosing.")
    print("Using command 'radio' displays signal strength for the location of Waldo's case")
    print("Using command 'bye' lets you quit the game, your progress will be saved to your username.")
    return


# Signaalin vahvuus print, näytölle syötteenä signal_strenght 1 - 5
def signal_strength_ascii(signal_strength):
    # ÄLÄ KOSKE TÄHÄN TÄMÄ ON TARKOITUKSELLA NÄIN KOSKA PRINT FUNKTIO PUSKEE SEN MUUTEN VÄÄRIN
    if signal_strength == 5:
        print('''
                     §§§§§§   
              §§§§§§ §§§§§§
       §§§§§§ §§§§§§ §§§§§§
§§§§§§ §§§§§§ §§§§§§ §§§§§§
§§§§§§ §§§§§§ §§§§§§ §§§§§§
Signal strength is excellent    ''')
    elif signal_strength == 4:
        print(''' 
                     ......
              §§§§§§ ......
       §§§§§§ §§§§§§ ......
§§§§§§ §§§§§§ §§§§§§ ......
§§§§§§ §§§§§§ §§§§§§ ......
Signal strength is strong    ''')
    elif signal_strength == 3:
        print('''  
                     ......
              ...... ......
       §§§§§§ ...... ......
§§§§§§ §§§§§§ ...... ......
§§§§§§ §§§§§§ ...... ......
Signal strength is medium    ''')
    elif signal_strength == 2:
        print('''   
                     ......        
              ...... ......
       ...... ...... ......
§§§§§§ ...... ...... ......
§§§§§§ ...... ...... ......
Signal strength is low    ''')
    elif signal_strength == 1:
        print(''' 
                     ......        
              ...... ......
       ...... ...... ......
...... ...... ...... ......
...... ...... ...... ......
Signal strength is weak    ''')


# Kuuma/kylmä mekaniikka joka vertaa edellistä etäisyyttä, nykyiseen etäisyyteen metreissä
def hot_cold_mechanic(case_icao_location, username, previous_distance_to_case):
    new_distance_tuple = database.database_query_fetchone(
        kyselyt.query_distance_between_player_locations(username, case_icao_location)
    )
    distance_to_case = new_distance_tuple[0]
    if previous_distance_to_case > distance_to_case:
        print("\nThe signal got stronger!")
        print("I think we're getting closer!, Waldo says")
        audio_library.play_waldo_sound(11)
    elif previous_distance_to_case < distance_to_case:
        print("\nThe signal has weakened!")
        print("Mmm... bad luck, Waldo says sadly")
        audio_library.play_waldo_sound(6)
    else:
        print("\nThe signal hasn't budged!")
        print("Signal's the same, Waldo says ")
        audio_library.play_waldo_sound(8)
    return distance_to_case


# Funktio tulostaa vihjeen sekä vastaavan maan asciin listasta, joka tulee sql kyselyn kautta
def country_clue(case_icao_location):
    clues_rows = database.database_query(kyselyt.query_country_hint(case_icao_location))
    clues_tuples = clues_rows[0] #PURETAAN ENSIMMÄINEN RIVI

    #Paluu on monikko jossa 0 = country hint, 1 = country name
    ascii_countries.country_art(clues_tuples[1].lower())
    print("\nCLUE:")
    print(clues_tuples[0])
    return


# Funktio ottaa käyttäjän syötteen ja jos syöte löytyy command monikosta palauttaa sen
# muuten printaan tuntematon komento ja kysytään syötettä uudestaan
def user_input_command(commands):
    user_input = None
    while user_input not in commands:
        user_input = input("Waldo asks: What do you wish to do next?: ").lower()
        if user_input not in commands:
            print("\nWaldo didn't understand that")
            print("If you need help type 'help'")
            audio_library.play_waldo_sound(3)
    return user_input


# Funktio tulostaa kaikki saatavilla olevat kohteet
def user_search(countries):
    #travel_ascii_art(5)
    print("\nAVAILABLE DESTINATIONS")
    for i in range(0,len(countries_list)-1,4):
        if i >= len(countries_list)-1:
            print(f"{countries_list[i]:25}")
        print(f" {countries_list[i]:25}{countries_list[i+1]:25}{countries_list[i+2]:25}{countries_list[i+3]:25}")
    return


# Funktio vertaa käyttäjän etäisyyttä laukkuun ja palauttaa sen mukaisen kuvan
def signal_strength(case_icao_location, username):
    distance_tuple = database.database_query_fetchone(kyselyt.query_distance_between_player_locations(username, case_icao_location))
    distance = distance_tuple[0]
    distance_kilometers = distance / 1000
    if distance_kilometers < 400:
        signal_strength_ascii(5)
        print("The case must be under a 400km radius")
    elif distance_kilometers < 800:
        signal_strength_ascii(4)
        print("The case must be under a 800km radius")
    elif distance_kilometers < 1200:
        signal_strength_ascii(3)
        print("The case must be under a 1200km radius")
    elif distance_kilometers < 1600:
        signal_strength_ascii(2)
        print("The case must be under a 1600km radius")
    elif distance_kilometers < 2000 or distance_kilometers > 2000:
        signal_strength_ascii(1)
        return


# Matkustus funktio, palauttaa matkustusmaan joka ei ole suomi, tai back palaa takaisin!
def travel(username, country_list):
    user_country = database.database_query_fetchone(kyselyt.query_fetch_user_country(username))
    audio_library.play_waldo_sound(13)
    while True:
        player_input = input("\nWaldo is excited! Where do you want to travel?: ").lower()
        if player_input == 'back':
            break
        elif player_input == "destinations":
            user_search(country_list)
            audio_library.play_waldo_sound(5)
        elif player_input == user_country[0]:
            print("Waldo is confused, we're here already! what do you mean?")
            print("Type 'back' to go to previous menu.")
            audio_library.play_waldo_sound(3)
        elif player_input not in country_list:
            print("Waldo is confused, what do you mean?")
            print("Type 'destinations' to see waldo's list of countries.")
            print("Type 'back' to go to previous menu.")
            audio_library.play_waldo_sound(3)
        else:
            break
    return player_input


#Ladataan käyttäjän arvot käyttäjänimen mukaan
def load_game(username):
    #game.id, game.location, suitcase.location, co2_consumed, total_kilometers, clue_unlocked, travel_count
    loaded_data_list = database.database_query(kyselyt.query_load_username(username))
    loaded_data_tuple = loaded_data_list[0]
    return loaded_data_tuple


#Arvotaan matkalaukulle maa ja icao
def case_randomizer():
    case_country = 'Finland'
    while case_country == 'Finland' or case_country == 'Russia':
        case_country = list_random(
            database.database_query(kyselyt.query_countries)
        )
    case_icao_location = list_random(
        database.database_query(kyselyt.query_country_airports(case_country))
    )
    return case_country, case_icao_location


# Pelin aloitus kysely
def start_game():
    while True:
        player_input = input("\nStart the game? yes/no: ").lower()
        if player_input != 'yes':
            print("\nWaldo looks at you with crying eyes, you need to help me!")
            audio_library.play_waldo_sound(2)
        else:
            break
    return


# Funktio jolla piirretään pilvet ja ilmoitetaan saapumisesta
def travel_ascii_art(ascii_num):
    if ascii_num == 5:
        print('''  
                                      *** MAP⠀***⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⡜⢎⣼⣰⡗⣖⡋⢦⡙⢎⡱⢿⣷⠒⠛⣶⡿⣟⣧⡏⢯⣿⣦ NORWAY⠀⠀⠀ ⠀⠀⠀⠀⠀⠀   FINLAND  ⠳⡜⣊⠶⢫⢫⣴⣿⣿⠙⣻⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ICELAND⢥⠳⡜⣊⠶⢫⢫⣴⣿⣿⠙⣻⠟⣌⠳⢣⡙⢦⡹⢌⡿⠗⠀⠀  SWEDEN⠀⠀⠀            ⠀⠀⠀⠀⠀⠀⠀⠀   ⣋⠼⣱ ⠀ 
        ⢚⡜⣣⢕⡫⢴ (Faroe Island)⢻⣌⡓⡣⢝⡢⢇⡫⡜⡶⣦⡶     ⡪⣾⠥⣋⡟⠲⣽⠆     ESTONIA⠀⠀⠀⠀⠀⠀⠀⠀ ⣋⠼⣱     ⠀⠀⠀
        ⣋⠼⣱⢪⡕⢣⡹⢰⢍⣓⡎⠝⣟⣿⣿⡂⡴⡏⢦⡓⡍⠶⣉⠶⡡⢇⢳⢢⣵⡟⣽⢟⣧⠀⠀⠀⢠⣏⢷⡋⣖⣹ ⠀  LATVIA⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣋⠼⣱ ⠀⠀⠀⠀⠀⠀⠀
        ⡝⢮⡱⢦⡙⢦⣵⢏⡾⠿⠛Isle of Man⢷⢣⡱⢊⡗⣩⠖⣍⢮⢱⢺⡟⢁⣿⣷⣞⡏⢠⡶⢾⡙⢦⢱⢢⡱ LITHUANIA⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣋⠼⣱ ⠀⠀
        ⡸⢇⡸⣆⠹⣶⣏⡀⠀⠀    ⠸⣆⠷⡉⣶⠱⡾⡈⢾  DENMARK  ⢿⠹⣿⣆⠹⣆⢷⣶⣿ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀BELARUS⠀⠀⠀    ⠀⣋⠼⣱ ⠀
        ⡹⢬⡑⡎⢵⣢IRELAND⣺     ⠀⠠⢼⡧⢱⡂⢟⡰⡙⢦⡑⢎⣽⠂⠛⣿⠽⠛⢿⣴⠜⠋⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⣋⠼⣱ 
        ⢕⡣⡝⡜⣩⠿⣤⠦⡖⢶⣋⣷ UNITED ⠐⠓⢧⡙⢦⢱⣿⡛⠛⠉  ⠀⠀⠀    ⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀    ⠀⠀  ⣋⠼⣱ 
        ⢪⠕⣎⠵⣃⠞⡤⢛⡌⢧⡘⢭⡷ KINGDOM ⣴⢯⡘⢦NETHERLANDS   ⠀⠀  POLAND⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀   ⣋⠼⣱  
        ⢎⡝⢦⡙⢦⠛⡴⣋⡜⣲⠿⠧⣴⠲⡖⢷⠲⣔⣺⠒⠋BELGIUM ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                ⠀⠀⠀⠀⠀⠀⠀⠀⠀ UKRAINE      ⡝⢮⡱   
        ⢮⡜⣣⠝⣪⣙⠲⡥⢚⡥⢚(Guernsay)⣎⣵⠂⠋ ⠀⠀   ⠀GERMANY⠀⠀⠀               ⠀⠀⠀⠀⠀       ⠀    ⠀⠀⠀       ⡸⢇⡸ ⠀ ⠀⠀
        ⢦⡙⢦⡛⡴⣡⢛⠼⡡⢞⣿⡉⠙⠻⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀   CZECH REPUBLIC⠀⠀SLOVAKIA⠀     MOLDOVA ⠀      ⡹⢬⡑    
        ⢖⡹⢦⡙⡖⣥(Jersey)⡜⡹⢷⡀⠀⠀⠀⠀  ⠀LUXEMBOURG⠀⠀     ⠀⠀⠀       ⠀⠀⠀     ⠀   ⠈⠉⠙⠒⠛⠁⣠⣒⣒⠫⣉⠛     ⣒⢕⡣⡝ 
        ⢋⡼⣡⢏⡜⢦⡙⠼⡱⣍⢲⡑⡫⢦⡀⠀⠀FRANCE⠀(Liechtenstein) AUSTRIA⠀ ⠀   HUNGARY            ⠱⣎⡝⢦⢣    ⢕⡣⡝ 
        ⣭⢲⡱⢎⡜⢦⡙⡥⠳⣌⠧⣜⠱⣪⢧⠀⠀⠀⠀⠀⠀SWITZERLAND⠀     SLOVENIA                                  ⢪⠕⣎          
        ⢴⢣⡜⠒⠛⠦⠧⣍⠳⡌⠶⣌⠳⡟⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⡽⣷⣷⡄  CROATIA⠀⠀⠀⠀⠀⠀⠀⠀⠀        ROMANIA      ⢎⡝⢦  
        ⢮⢱⡟⠀⠀⠀⠀⠀⠈⠉⠙⠒⠛⠁⠀⠀⠀⠀ANDORRA⠀ ⣴⡛⠶⡄⠀⠀⠉⢷⡌⡽⢫⣆⣀⠀⠀⠀⠀⠀⠀CROATIA⠀ ⠀SERBIA                ⢮⡜⣣         
        ⠦⣻⠁⠀⠀SPAIN⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾(Monaco)⢾⠱⣬⡷⢽⣆⠀⠀⠱⡜⡥⢚⡟⢿⠦⣄⡀MONTENEGRO    KOSOVO            ⢦⡙⢦     
        ⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⢟⡡⢏⢎⠳⡙⣎⠹⡇(San Marino)⠓⣎⠧⣚⠴⡹⠂⠀BOSNIA       MACEDONIA       ⢖⡹⢦    
        ⠁        ⠀⠀⠀⠀⠀⠀⣠⠞⣇⠳⡸⡌⢵⢊⠮⣱⠙⣆⣯⠟⢹⡆⣓⠦ ITALY⠀⠀⣩⣚⢶⣙⣄⠀⠀⠀⠘⠷⠿⡓        ⠀      BULGARIA  ⢋⡼⣡     
        PORTUGAL⠀⠀⠀  ⠀⠀⢸⣡⠫⡔⣷⢟⡞⢿⢊⡵⢊⡽⣠⢻⠀⢸⡜⢢(Vatican City)⣓⡱⢍⡲⠀⠼⣷⢽⡢⢣⢯ALBANIA            ⣭⢲⡱        
        ⢆⡤   ⠀⠀⠀⠀⠀⠀⠀⣠⡖⢇⡣⢭⡙⢧⡙⢆⡫⢔⠫⣔⢣ MALTA ⠭⡜⢎⣼⣰⡗⣖⡋⢦⡙⢎⡱⢿⣷⠒⠛⣶⡿⣟⣧⡏⢯⣿⣦⣤       GREECE  ⢴⢣⡜      
        ⣕(Gibraltar)⣝⡪⣚⣄⣃⣢⣄⣘⣉⣲⣦⣉⣆⣩⣂⣅⣇⣜⣠⣌⣪⣝⣆⣣⣍⣷⣼⣜⣰⣃⣞⣢⣝⣦⣙⣙⣆⣛⣌⣞⣤⣓⣜⣫⣙⣬⣓⣜⣆⣳⣥⣛⣔⣫⣱⣌⣳⣉⣎
                ''')
    if ascii_num == 4:
        #   •   Green: "\033[32m
        #   •   Yellow: \033[33m
        #   •   Blue: \033[34m
        #   •   Magenta: \033[35m
        #   •   Cyan: \033[36m
        #   •   White: \033[37m
        #   •   Reset (to go back to the normal color): \033[0m
        #	•	90: Bright Black (gray)
        #	•	91: Bright Red
        #	•	92: Bright Green
        #	•	93: Bright Yellow
        #	•	94: Bright Blue
        #	•	95: Bright Magenta
        #	•	96: Bright Cyan
        #	•	97: Bright White
        print('''
        
  \033[32m` : | | | |:  ||  :     `  :  |  |+|: | : : :|   .        `              .\033[0m
      \033[32m` : | :|  ||  |:  :    `  |  | :| : | : |:   |  .                    :\033[0m
         \033[32m.' ':  ||  |:  |  '       ` || | : | |: : |   .  `           .   :.\033[0m
                \033[32m`'  ||  |  ' |   \033[33m*\033[0m    \033[32m` : | | :| |\033[33m*\033[0m  \033[32m|:   :               :|\033[0m
        \033[33m*    *\033[0m      \033[32m `  |  : :  |  .      ` ' :| | :| . : :         \033[33m*\033[0m   \033[32m:.||\033[0m
             .`            \033[32m| |  |  : .:|       ` | || | : |: |          | ||\033[0m
      '          .         \033[33m+\033[0m \033[32m`  |  :  .: .         '| | : :| :    .   |:| ||\033[0m
         .                 .    ` \033[33m*\033[0m\033[32m|  || :       `    | | :| | :      |:| |\033[0m
 .                .          .        \033[32m|| |.: \033[33m*\033[0m          \033[32m| || : :     :|||\033[0m
        .            .   . \033[33m*\033[0m    .   .  ` \033[32m|||.  +        + '| |||  .  ||`\033[0m
     .             \033[33m*\033[0m              .     \033[32m+:`|!             . ||||  :.||`\033[0m
 \033[33m+\033[0m                      .                \033[32m..!|*          . | :`||+ |||`\033[0m
     .                         \033[33m+\033[0m      \033[32m: |||`        .| :| | | |.| ||`\033[0m     .
       \033[33m*\033[0m     \033[33m+\033[0m   '               \033[33m+\033[0m  \033[32m:|| |`     :.+. || || | |:`|| `\033[0m
                            .      \033[32m.||` .    ..|| | |: '` `| | |`\033[0m  \033[33m*\033[0m
  .       \033[33m+++\033[0m                      \033[32m||        !|!: `       :| |\033[0m
              \033[33m+\033[0m         .      .    \033[32m| .      `|||.:      .||\033[0m    .      .    `
          '                           \033[32m`|.   .  `:|||   + ||'\033[0m     `
      \033[33m+\033[0m      \033[34m\033[33m*\033[34m                         \033[32m`'       `'|.    `:\033[0m
\033[34m"'  `---"""----....____,..^---`^``----.,.___          `.    `.  .    ____,.,-
    ___,--'""`---"'   ^  ^ ^        ^       """'---,..___ __,..---""'
--"'                           ^                         ``--..,__ D. Rice''')
    if ascii_num == 3:
        print('''
            ^^                   @@@@@@@@@
       ^^       ^^            @@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@              ^^
                           @@@@@@@@@@@@@@@@@@@@
 ~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~~~ ~~~
 ~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~       ~~     ~~ ~
   ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~     ~~~    ~ ~~~  ~ ~~
   ~  ~~     ~         ~      ~~~~~~  ~~ ~~~       ~~ ~ ~~  ~~ ~
 ~  ~       ~ ~      ~           ~~ ~~~~~~  ~      ~~  ~             ~~
       ~             ~        ~      ~      ~~   ~             ~''')

    if ascii_num == 2:
        print('''
                        _                                  
              (`  ).                   _           
             (     ).              .:(`  )`.       
)           _(       '`.          :(   .    )      
        .=(`(      .   )     .--  `.  (    ) )      
       ((    (..__.:'-'   .+(   )   ` _`  ) )                 
`.     `(       ) )       (   .  )     (   )  ._   
  )      ` __.:'   )     (   (   ))     `-'.-(`  ) 
)  )  ( )       --'       `- __.'         :(      )) 
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'          

--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.''')

    if ascii_num == 1:
        print('''
              .

              |					
     .               /				
      \       I     				
                  /
        \  ,g88R_
          d888(`  ).                   _
 -  --==  888(     ).=--           .+(`  )`.
)         Y8P(       '`.          :(   .    )
        .+(`(      .   )     .--  `.  (    ) )
       ((    (..__.:'-'   .=(   )   ` _`  ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (   ))     `-'.:(`  )
)  )  ( )       --'       `- __.'         :(      ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'

--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.''')
    return


#Luodaan lista pelin maista ja palautetaan se
def game_countries_list():
    countries_list = []
    for country in database.database_query(kyselyt.query_countries):
        if country[0] != 'Finland' and country[0] != 'Russia':
            countries_list.append(country[0].lower())
    return countries_list

#Hakee pelaajat järjestyksessä löydettyjen matkalaukkujen perusteella
def leaderboard():

    print("---------------LEADERBOARD------------------")
    for player_stats in database.database_query(kyselyt.sql_query_fetch_leaderboards):
        print(f"Suitcases found: {player_stats[1]} by {player_stats[0].upper()}")
    print("--------------------------------------------")
    return

#Valintarakenne lataa, tai aloita uusi peli. uudessa pelissä lisää tietokantaan pelaajan
def load_or_new_game():
    while True:
        new_game = input("\nStart a 'new' or 'load' an existing game: ").lower()
        if new_game != 'load' and new_game != 'new':
            print("Unknown command!")
        # Uusi käyttäjä, kysytään nimi asetetaan alkuarvot tietokantaan
        elif new_game == 'new':
            username = input("\nWaldo greets you! Enter new player name: ").lower()
            username_exist = database.database_check_query(kyselyt.query_check_username(username))
            if username == 'back':
                continue
            elif username_exist:
                    print("Name already taken!")
            elif not username_exist:
                # Asetetaan alkuarvot tietokantaan
                database.database_update(kyselyt.query_new_username(username))
                database.database_update(kyselyt.query_new_suitcase(username))
                # Arvotaan matkalaukun maa, ja sen jälkeen arvotaan matkalaukun ICAO
                case_country, case_icao_location = case_randomizer()
                database.database_update(kyselyt.query_update_suitcase_location(case_icao_location, username))
                return username

        elif new_game == 'load':  # Load previous game
            users_list = database.database_query(kyselyt.sql_query_fetch_users)
            print("\n-----List of users------")
            for user in users_list:
                print(user[0].upper())
            print("------------------------")
            username = input("\nWaldo greets you! Enter player name: ").lower()
            username_exist = database.database_check_query(kyselyt.query_check_username(username))
            if username == 'back':
                continue
            elif not username_exist:
                print("Name doesn't exist")
            elif username_exist:
                return username

#Kuuma/kylmää varten lasketaan etäisyys pelaajan ja matkalaukun välillä, käytetään setupissa
def base_suitcase_distance():
    distance_tuple = database.database_query_fetchone(
        kyselyt.query_distance_between_player_locations(username, case_icao_location))
    return distance_tuple[0]



#"Yleiset arvot"
#Määritetään vakio komennot monikkoon
commands = ("clue", "destinations", "travel", "radio", "help", "bye", "joke")
#case_country, case_icao_location, username, user_command, travel_country


#Lista pelin maista joihin helppo verrata, listassa on eroteltu suomi pois 'lähtömaa'
countries_list = game_countries_list()

clear_screen()
print('''You've arrived at Helsinki-Vantaa airport, where you meet your good friend Waldo.

Waldo is a world-famous adventurer known for his red & white striped shirt and blue hat.
He has travelled all over the european continent, but his valuable suitcase mysteriously disappeared. 
The suitcase contained Waldo's most important discoveries and notes, but fortunately, Waldo has installed a radio-transmitter in it.

Now Waldo needs your help to find his suitcase. 
Together, you set off around europe, using the radio-transmitter in the suitcase. 

Safe travels!\n''')

#Haluatko aloittaa pelin funktio
help()
start_game()
audio_library.play_game_sound(6) #Start game ääni
clear_screen()
animations.waldo_animated() #Intro animaatio

leaderboard()
audio_library.play_waldo_sound(10)

#Load or new game valinta josta palautetaan käyttäjänimi peliä varten
username = load_or_new_game()


#Ladataan pelin tila ja puretaan se muuttujiin
data_tuple = load_game(username)
#game.id, game.location, suitcase.location, co2_consumed, total_kilometers, clue_unlocked, travel_count
username = data_tuple[0]
player_country_icao = data_tuple[1]
case_icao_location = data_tuple[2]
co2_consumed = data_tuple[3]
total_kilometers = data_tuple[4]
clue_reminder_given = data_tuple[5]
travel_counter = data_tuple[6]



# Asetetaan Vakioarvot pelin alussa
last_joke = joke_int = 0
travel_counter_limit = 5
goal_reached_bool = False

#Lasketaan alkusijainti, ja asetetaan se base-etäisyydeksi kuuma/kylmää varten
previous_distance_to_case = base_suitcase_distance()

#Päivitetään ruutu
clear_screen()


#PELI ALKAA MAIN GAME LOOP TÄSSÄ
print("\nWell let's get going!")
audio_library.play_waldo_sound(4)
travel_ascii_art(5)

user_command = None
while user_command != 'bye':


    #Jos pelaaja on saavuttanut tavoitteen printataan voitto ruutu
    if goal_reached_bool:

        # Voittoprintti tähän!
        clear_screen()
        travel_ascii_art(4)
        audio_library.play_game_sound(1)


        #Ladataan tietokannasta, kilometrit ja travel count voitto printtiä varten.
        data_tuple = load_game(username)
        total_kilometers = data_tuple[4]
        travel_counter = data_tuple[6]


        # Profiilin reset, valmiiksi uutta peli kertaa varten
        database.database_update(kyselyt.query_reset_game_state(
            username))  # Resetataan peli pelaajan osalta ja lisätään tilastoihin 1 matkalaukku löydetty
        case_country, case_icao_location = case_randomizer()  # Asetetaan uusi matkalaukku myös seuraavaa pelikertaa varten
        database.database_update(kyselyt.query_update_suitcase_location(case_icao_location, username))


        # Onnittelu teksti
        animations.print_congratulations(
            f"CONGRATULATIONS!!! You've found Waldo's suitcase in {travel_country.upper()}. A point has been added to your record!")
        animations.display_results(total_kilometers, travel_counter)  # Voittoruutu
        audio_library.play_game_sound(8)  # You're the best!


        # Jos pelaaja haluaa jatkaa peliä
        if input("\nType 'yes' to play again: ").lower() != 'yes':
            print("Thank you for playing!")
            break  # Poistutaan peli loopista kokonaan jos ei
        else:
            previous_distance_to_case = base_suitcase_distance() #Kuuma/kylmä reset
            goal_reached_bool = False  # Vakio arvojen resetointi, jos peli jatkuu suoraan
            clue_reminder_given = 0
            travel_counter = 0
            player_country_icao = 'EFHK' #Hardcode HEL koska wäääääää!

            #Näkymän resetointi
            clear_screen()
            travel_ascii_art(5)


    #Jos käyttäjä on matkustanut tarpeeksi askelia ilmoitetaan vihjeen saatavuudesta
    if travel_counter >= travel_counter_limit and clue_reminder_given == 0:
        print("\nHey!!!! WAIT A MINUTE!")
        audio_library.play_game_sound(1)
        print("Waldo looks at you and says, I guess I remember a little riddle from the country")
        audio_library.play_waldo_sound(7)

        #Asetetaan vihje annetuksi ja päivitetään tietokantaan myös
        clue_reminder_given = 1
        database.database_update(kyselyt.query_update_clue_unlocked(username, clue_reminder_given))


    #Printtiä varten näytetään missä maassa pelaaja on tällä hetkellä
    user_country = database.database_query_fetchone(kyselyt.query_fetch_user_country(username))
    print(f"\nYou are currently in {user_country[0].upper()} with Waldo!")
    user_command = user_input_command(commands)   #Kysytään käyttäjän input funktiolla


    ##Vihje funktio,  joka tulostaa maan vihjeen perustuen matkalaukun ICAO sijaintiin (case_location)
    if user_command == commands[0]:  #VIHJE
        if clue_reminder_given == 1:
            country_clue(case_icao_location)
        else:
            print("\nWaldo's memory is still a bit hazy, maybe later")
            print("Maybe a 'joke' could refresh his mind up!")
            audio_library.play_waldo_sound(3)


    #Kohteet funktio,  kohteiden näyttäminen käyttäjälle (tällä hetkellä pelkät maat)
    elif user_command == commands[1]: #KOHTEET
        user_search(countries_list)
        audio_library.play_waldo_sound(5)


    #Matkustus tapahtumat, MAAN VALINTA, SITTEN, PÄIVITYS TIETOKANTAAN, +1 TRAVEL JA KUUMA/KYLMÄ LASKENTA
    elif user_command == commands[2]: #MATKUSTUS

        #Kutsutaan matkustus funktiota ja otetaan matkustus maa talteen paluuna
        travel_country = travel(username, countries_list)
        if travel_country != 'back':  #Palataan takaisin jos komento 'back'

            #Otetaan talteen maa mistä lähdetään, myöhempää laskentaa varten
            previous_country_icao = player_country_icao
            country_icaos_list = database.database_query(kyselyt.query_country_airports(travel_country))  #Icaot tulevaisuutta ajatellen jos laajenee lentokenttiin
            country_icao_tuple = country_icaos_list[0] #Maan ICAO - tarvitaan seuraavaa päivityskyselyä varten
            player_country_icao = country_icao_tuple[0]

            #Matkustus animaatio ja ääni!
            clear_screen()
            animations.start_travel_animation(travel_country)
            audio_library.play_game_sound(5)
            clear_screen()

            #Lasketaan kilometrit matkalta ja otetaan ylös
            kilometers = kilometer_counter(player_country_icao, previous_country_icao) #Kilometrien laskenta
            travel_counter += 1

            #Päivitetään arvot kilometrit ja co2, travel_count eli +1, ja location pelaajan tietokantaan
            database.database_update(kyselyt.query_update_player_travel(username, kilometers, 1, player_country_icao))

            #Tarkistetaan onko pelaaja saavuttanut tavoitetta eli sama maa kun laukku
            goal_reached_bool = goal_check(username)

            if not goal_reached_bool:
                # Kuuma/kylmä mekaniikka jos ei ole saavuttanut tavoitetta
                travel_ascii_art(5)  # Kartan printtaus
                previous_distance_to_case = hot_cold_mechanic(case_icao_location, username,
                                                              previous_distance_to_case)
                signal_strength(case_icao_location, username)  # Signaalin printtaus



    #Radio komento signaalin vahvuuden tulostamiseen
    elif user_command == commands[3]: #RADIO
        signal_strength(case_icao_location, username)
        audio_library.play_game_sound(3) #Radio ääni


    #Help komento, tulostetaan help print
    elif user_command == commands[4]:
        help() #Help-komento
        audio_library.play_game_sound(2) #Help ääni


    #Joke komento, pieni hauskuus
    elif user_command == commands[6]:
        while last_joke == joke_int:
            joke_int = random.randint(1, 10)
        last_joke = joket.joke_for_waldo(joke_int)
        audio_library.play_waldo_sound(14)


#Jos pelaaja lähtee kesken pelin!
if user_command == 'bye':
    print("\nWaldo is furious!!")
    audio_library.play_waldo_sound(12)
