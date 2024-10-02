#Peliä varten täytyy asentaa mysql-connector-python 8.0.29!!!
#Peliä varten täytyy asentaa playsound, ja pyfiglet

#Yhteyden luonti tietokantaan erillisessä filessä
#Importataan kyselyt.py ja database.py ja random, audio ja animations
import database
import kyselyt
import random
import animations
import audio_library


#Importataan tähän eri aliohjelmat ja kyselyaliohjelmat yms
#Liimaillaan parhaamme mukaan ja tsemppiä :)

#ALIOHJELMAT LÖYTYVÄT TÄSTÄ

def clear_screen():
    print('\n' * 50)
    return

#Funktio jolla tarkastetaan onko pelaaja löytänyt matkalaukun maan
def goal_check(username, case_location):
    user_country = database.database_query_fetchone(kyselyt.query_fetch_user_country(username))
    if user_country[0] == case_location:
        return True
    else:
        return False

# ottaa listan ja arpoo jonkun arvon listasta
def case_randomizer(list):
    random_index = random.randint(0, len(list)-1)
    random_str = list[random_index]
    return random_str[0]


#Kysytään käyttäjän nimi, ja palautetaan jos se on uniikki, päivitetään se tietokantaan
def input_username():
    username_exist = True
    while username_exist:
        username = input("\nWaldo greets you! Enter new player name: ").lower()
        username_exist = database.database_check_query(kyselyt.query_check_username(username))
        if username_exist:
            print("\nName already taken!")
    database.database_update(kyselyt.query_new_username(username))
    return username

#Kilometrilaskuri laskee edellisen icaon ja uuden paikan välin kilometrit kyselyn avulla
def kilometer_counter(username, previous_icao):
    meters_tuple = database.database_query_fetchone(kyselyt.query_distance_between_locations(username,previous_icao))
    kilometers = meters_tuple[0] / 1000
    return kilometers


#tulostaa komennot käyttäjälle
def help():
    #print("\nUsing command 'help' opens this window.")
    print("\nUsing command 'clue' gives you a clue.")
    print("Using command 'destinations' prints the country's you can travel to.")
    print("Using command 'travel' travels you to your country of choosing.")
    print("Using command 'radio' displays signal strength for the location of Waldo's case")
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
        kyselyt.query_distance_between_locations(username, case_icao_location)
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


# Funktio tulostaa vihjeen listasta, joka tulee sql kyselyn kautta
def country_clue(case_icao_location):
    clue = database.database_query(kyselyt.query_country_hint(case_icao_location))
    print("\nCLUE:")
    for clue in clue:
        print(clue[0])
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
    distance_tuple = database.database_query_fetchone(kyselyt.query_distance_between_locations(username, case_icao_location))
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
        ⢖⡹⢦⡙⡖⣥(Jersey)⡜⡹⢷⡀⠀⠀⠀⠀  ⠀LUXEMBURG⠀⠀     ⠀⠀⠀       ⠀⠀⠀     ⠀   ⠈⠉⠙⠒⠛⠁⣠⣒⣒⠫⣉⠛     ⣒⢕⡣⡝ 
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
        print('''
  ` : | | | |:  ||  :     `  :  |  |+|: | : : :|   .        `              .
      ` : | :|  ||  |:  :    `  |  | :| : | : |:   |  .                    :
         .' ':  ||  |:  |  '       ` || | : | |: : |   .  `           .   :.
                `'  ||  |  ' |   *    ` : | | :| |*|  :   :               :|
        *    *       `  |  : :  |  .      ` ' :| | :| . : :         *   :.||
             .`            | |  |  : .:|       ` | || | : |: |          | ||
      '          .         + `  |  :  .: .         '| | : :| :    .   |:| ||
         .                 .    ` *|  || :       `    | | :| | :      |:| |
 .                .          .        || |.: *          | || : :     :|||
        .            .   . *    .   .  ` |||.  +        + '| |||  .  ||`
     .             *              .     +:`|!             . ||||  :.||`
 +                      .                ..!|*          . | :`||+ |||`
     .                         +      : |||`        .| :| | | |.| ||`     .
       *     +   '               +  :|| |`     :.+. || || | |:`|| `
                            .      .||` .    ..|| | |: '` `| | |`  +
  .       +++                      ||        !|!: `       :| |
              +         .      .    | .      `|||.:      .||    .      .    `
          '                           `|.   .  `:|||   + ||'     `
  __    +      *                         `'       `'|.    `:
"'  `---"""----....____,..^---`^``----.,.___          `.    `.  .    ____,.,-
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


#"Yleiset arvot"
#Määritetään vakio komennot monikkoon
commands = ("clue", "destinations", "travel", "radio", "help", "bye")
#case_country, case_icao_location, username, user_command, travel_country


#Lista pelin maista joihin helppo verrata, listassa on eroteltu suomi pois 'lähtömaa'
countries_list = []
for country in database.database_query(kyselyt.query_countries):
    if country[0] != 'Finland' and country[0] != 'Russia':
        countries_list.append(country[0].lower())

clear_screen()
print('''You've arrived at Helsinki-Vantaa airport, where you meet your good friend Waldo.

Waldo is a world-famous adventurer known for his red & white striped shirt and blue hat. He has travelled all over the european continent, but his valuable suitcase mysteriously disappeared. 
The suitcase contained Waldo's most important discoveries and notes, but fortunately, Waldo has installed a radio-transmitter in it.

Now Waldo needs your help to find his suitcase. Together, you set off around europe, using the radio-transmitter in the suitcase. 

Safe travels!\n''')

#Haluatko aloittaa pelin funktio
help()
start_game()
audio_library.play_game_sound(6) #Start game ääni
clear_screen()
animations.waldo_animated() #Intro animaatio

#Asetetaan Vakioarvot pelin alussa
goal_reached_bool = False
clue_reminder_given_bool = False
total_kilometers = 0
country_icao_tuple = ('EFHK',)
travel_counter = 0
travel_counter_limit = random.randint(4,6)

#Arvotaan matkalaukun maa, ja sen jälkeen arvotaan matkalaukun ICAO
case_country = 'Finland'
while case_country == 'Finland' or case_country == 'Russia':
    case_country = case_randomizer(
        database.database_query(kyselyt.query_countries)
    )
case_icao_location = case_randomizer(
    database.database_query(kyselyt.query_country_airports(case_country))
)

#print(case_icao_location, case_country) #TÄMÄ ON DEVAUSTA VARTEN MUISTA KOMMENTOIDA POIS!

#Pelin alustus, kysytään käyttäjän nimi ja tarkistetaan onko se uniikki
#Syötetään käyttäjänimi tietokantaan ID, LOCATION vakio 'EFHK' game taulu
audio_library.play_waldo_sound(10)
username = input_username()

#Kutsutaan help alkuun pelaajalle, ohjeistukseen liittyen
clear_screen()
#help()

#Lasketaan alkusijainti, ja asetetaan se base-etäisyydeksi kuuma/kylmää varten, asetetaan se muuttujaan
distance_tuple = database.database_query_fetchone(kyselyt.query_distance_between_locations(username, case_icao_location))
previous_distance_to_case = distance_tuple[0]

#PELI ALKAA MAIN GAME LOOP TÄSSÄ
print("\nWell let's get going!")
audio_library.play_waldo_sound(4)
travel_ascii_art(5)

user_command = None
while user_command != 'bye':

    #Jos käyttäjä on matkustanut tarpeeksi askelia ilmoitetaan vihjeen saatavuudesta
    if travel_counter >= travel_counter_limit and not clue_reminder_given_bool:
        print("\nHey!!!! WAIT A MINUTE!")
        audio_library.play_game_sound(1)
        print("Waldo looks at you and says, I guess i remember a little riddle from the country")
        audio_library.play_waldo_sound(7)
        clue_reminder_given_bool = True

    user_country = database.database_query_fetchone(kyselyt.query_fetch_user_country(username))
    print(f"\nYou are currently in {user_country[0].upper()} with Waldo!")
    user_command = user_input_command(commands)   #Kysytään käyttäjän input funktiolla


    ##Vihje funktio,  joka tulostaa maan vihjeen perustuen matkalaukun ICAO sijaintiin (case_location)
    if user_command == commands[0]:  #VIHJE
        if travel_counter >= travel_counter_limit:
            country_clue(case_icao_location)
        else:
            print("Waldo's memory is still a bit hazy, maybe later")
            audio_library.play_waldo_sound(3)

    #Kohteet funktio,  kohteiden näyttäminen käyttäjälle (tällä hetkellä pelkät maat)
    elif user_command == commands[1]: #KOHTEET
        travel_ascii_art(5)
        user_search(countries_list)
        audio_library.play_waldo_sound(5)

    #Matkustus tapahtumat, MAAN VALINTA, SITTEN, PÄIVITYS TIETOKANTAAN, +1 TRAVEL JA KUUMA/KYLMÄ LASKENTA
    elif user_command == commands[2]: #MATKUSTUS

        #Näytetään käyttäjälle kohteet minne matkustaa
        #clear_screen()
        #travel_ascii_art(5)

        #Kutsutaan matkustus funktiota ja otetaan matkustus maa talteen paluuna
        travel_country = travel(username, countries_list)
        if travel_country != 'back':

            #Otetaan talteen maa mistä lähdetään, myöhempää laskentaa varten
            previous_country_icao = country_icao_tuple[0]
            country_icaos_list = database.database_query(kyselyt.query_country_airports(travel_country))  #Icaot tulevaisuutta ajatellen jos laajenee lentokenttiin
            country_icao_tuple = country_icaos_list[0] #Maan ICAO - tarvitaan seuraavaa päivityskyselyä varten

            #LOCATION PÄIVITTÄMINEN PELAAJALLE TIETOKANTAAN, JA PRINTTAUS MATKUSTUKSESTA
            database.database_update(kyselyt.query_update_location(country_icao_tuple[0], username))
            clear_screen()

            #Matkustus animaatio ja ääni!
            animations.start_travel_animation(travel_country)
            audio_library.play_game_sound(5)
            clear_screen()

            travel_counter += 1  #Matkustus laskuriin lisätään 1 kerta

            #Lasketaan kilometrit matkalta ja otetaan ylös
            kilometers = kilometer_counter(username, previous_country_icao) #Kilometrien laskenta
            total_kilometers = total_kilometers + kilometers #total counter

            #Tarkistetaan onko pelaaja saavuttanut tavoitetta eli sama maa kun laukku
            goal_reached_bool = goal_check(username, case_country.lower())

            #Kuuma/kylmä mekaniikka jos ei ole saavuttanut tavoitetta
            if not goal_reached_bool:
                travel_ascii_art(5)
                previous_distance_to_case = hot_cold_mechanic(case_icao_location, username, previous_distance_to_case)
                signal_strength(case_icao_location, username)
            else:
                break #Siirrytään loopista ulos voittoprinttiin

    #Radio komento signaalin vahvuuden tulostamiseen
    elif user_command == commands[3]: #RADIO
        signal_strength(case_icao_location, username)
        audio_library.play_game_sound(3) #Radio ääni

    #Help komento, tulostetaan help print
    elif user_command == commands[4]:
        help() #Help-komento
        audio_library.play_game_sound(2) #Help ääni



#Jos pelaaja lähtee kesken pelin!
if not goal_reached_bool:
    print("\nWaldo is furious!!")
    audio_library.play_waldo_sound(12)


clear_screen()
#Voittoprintti tähän!
travel_ascii_art(4)
#Lisätään tietokantaan pelaajan co2 määrä
database.database_query(kyselyt.query_update_co2_total_player(username, int(total_kilometers * 8)))
audio_library.play_game_sound(1)   
animations.print_congratulations(f"CONGRATULATIONS!!! You've found Waldo's suitcase in {travel_country.upper()}.")
animations.display_results(total_kilometers, travel_counter) #Voittoruutu
audio_library.play_game_sound(8) #You're the best!