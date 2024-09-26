




#Signaalin vahvuus print, näytölle syötteenä signal_strenght 1 - 5
def signal_strength_ascii(signal_strength):
    #ÄLÄ KOSKE TÄHÄN TÄMÄ ON TARKOITUKSELLA NÄIN KOSKA PRINT FUNKTIO PUSKEE SEN MUUTEN VÄÄRIN
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
              §§§§§§ 
       §§§§§§ §§§§§§ 
§§§§§§ §§§§§§ §§§§§§ 
§§§§§§ §§§§§§ §§§§§§ ______
Signal strength is strong    ''')
    elif signal_strength == 3:
        print('''           
                      
       §§§§§§ 
§§§§§§ §§§§§§ 
§§§§§§ §§§§§§ ______ ______
Signal strength is medium    ''')
    elif signal_strength == 2:
        print('''            
                
               
§§§§§§ 
§§§§§§ ______ ______ ______
Signal strength is low    ''')
    elif signal_strength == 1:
        print('''                  
                                   
                                   
        
______ ______ ______ ______
Signal strength is weak    ''')



#Kuuma/kylmä mekaniikka joka vertaa edellistä etäisyyttä, nykyiseen etäisyyteen metreissä
def hot_cold_mechanic(distance_to_case, previous_distance_to_case):
    if previous_distance_to_case > distance_to_case[0]:
        print("\nThe signal got stronger!")
        print("I think we are getting closer!, Waldo says")
    elif previous_distance_to_case < distance_to_case[0]:
        print("\nThe signal has weakened!")
        print("Mmm... bad luck, Waldo says sadly")
    else:
        print("\nThe signal hasn't budged!")
        print("Same as before, Waldo says ")
    return



#Funktio tulostaa vihjeen listasta, joka tulee sql kyselyn kautta
def country_clue(clue):
    print("\nCLUE:")
    for clue in clue:
        print(clue[0])
    return


# Funktio ottaa käyttäjän syötteen ja jos syöte löytyy command monikosta palauttaa sen
# muuten printaan tuntematon komento ja kysytään syötettä uudestaan
def user_command(commands):
    user_input = None
    while user_input not in commands:
        user_input = input("\nWaldo asks: What do you wish to do next?: ").lower()
        if user_input not in commands:
            print("\nWaldo didn't understand that")
            print("If you need help type 'help'")
    return user_input



# Funktio tulostaa kaikki saatavilla olevat kohteet
def user_search(countries):
    print("\nAVAILABLE DESTINATIONS")
    for country in countries:
        print(country)
    return


#Funktio vertaa käyttäjän etäisyyttä laukkuun ja palauttaa sen mukaisen kuvan
def signal_strength(user_distance_from_case):
    distance = user_distance_from_case[0]
    if distance[0] < 400000:
        signal_strength_ascii(5)
    elif distance[0] < 800000:
        signal_strength_ascii(4)
    elif distance[0] < 1200000:
        signal_strength_ascii(3)
    elif distance[0] < 1600000:
        signal_strength_ascii(2)
    elif distance[0] <2000000 or distance[0] > 2000000:
        signal_strength_ascii(1)
        return

#Matkustus funktio, palauttaa matkustusmaan joka ei ole suomi!
def travel(country_list, user_country):
    while True:
        player_input = input("Waldo is excited! Where do you want to travel?: ").lower()
        if player_input == user_country:
            print("Waldo is confused, we are here already! what do you mean?")
        elif player_input not in country_list:
            print("Waldo is confused, what do you mean?")
        else:
            break
    return player_input

#Pelin aloitus kysely
def start_game():
    while True:
        player_input = input("Start the game? yes/no: ").lower()
        if player_input != 'yes':
            print("\nWaldo looks at you with crying eyes, you need to help me!")
        else:
            break
    return

#Funktio jolla piirretään pilvet ja ilmoitetaan saapumisesta
def travel_ascii(country,ascii_num):
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
    print(f"You have arrived in {country.upper()} with Waldo!")
    return

