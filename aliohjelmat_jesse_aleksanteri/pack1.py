




#Signaalin vahvuus print, näytölle syötteenä signal_strenght 1 - 5
def signal_strength_ascii(signal_strength):
    if signal_strength == 5:
        print('''            §§§§§§
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
    elif previous_distance_to_case < distance_to_case[0]:
        print("\nThe signal has weakened!")
    else:
        print("\nThe signal hasn't budged!")
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
        user_input = input("Waldo asks: What do you wish to do next?: ").lower()
        if user_input not in commands:
            print("Waldo didn't understand that")
    return user_input



# Funktio tulostaa kaikki saatavilla olevat kohteet
def user_search(countries):
    print("\n AVAILABLE DESTINATIONS")
    for country in countries:
        print(country[0])
    return



def signal_strength(user_distance_from_case):
    distance = user_distance_from_case[0]
    if distance[0] < 400000:
        signal_strength_ascii(5)
    elif distance[0] < 800000:
        signal_strength_ascii(4)
    elif distance[0] < 120000:
        signal_strength_ascii(3)
    elif distance[0] < 160000:
        signal_strength_ascii(2)
    elif distance[0] <2000000 or distance[0] > 2000000:
        signal_strength_ascii(1)
        return








