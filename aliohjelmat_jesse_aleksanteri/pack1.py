




#Signaalin vahvuus print, näytölle syötteenä signal_strenght 1 - 5
def signal_strength_ascii(signal_strength):
    if signal_strength == 5:
        print("                     §§§§§§")
        print("              §§§§§§ §§§§§§")
        print("       §§§§§§ §§§§§§ §§§§§§")
        print("§§§§§§ §§§§§§ §§§§§§ §§§§§§")
        print("§§§§§§ §§§§§§ §§§§§§ §§§§§§")
    elif signal_strength == 4:
        print("                    ")
        print("              §§§§§§")
        print("       §§§§§§ §§§§§§")
        print("§§§§§§ §§§§§§ §§§§§§")
        print("§§§§§§ §§§§§§ §§§§§§ ______")
    elif signal_strength == 3:
        print("             ")
        print("             ")
        print("       §§§§§§")
        print("§§§§§§ §§§§§§")
        print("§§§§§§ §§§§§§ ______ ______")
    elif signal_strength == 2:
        print("      ")
        print("      ")
        print("      ")
        print("§§§§§§")
        print("§§§§§§ ______ ______ ______")
    elif signal_strength == 1:
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("______ ______ ______ ______")



#Kuuma/kylmä mekaniikka joka vertaa edellistä etäisyyttä, nykyiseen etäisyyteen metreissä
def hot_cold_mechanic(distance_to_case, previous_distance_to_case):
    if previous_distance_to_case > distance_to_case[0]:
        print("\nSignaali vahveni!")
    elif previous_distance_to_case < distance_to_case[0]:
        print("\nSignaali heikkeni!")
    else:
        print("\nSignaali ei muuttunut")
    return



#Funktio tulostaa vihjeen listasta, joka tulee sql kyselyn kautta
def country_clue(clue):
    print("\nVIHJE:")
    for clue in clue:
        print(clue[0])
    return


# Funktio ottaa käyttäjän syötteen ja jos syöte löytyy command monikosta palauttaa sen
# muuten printaan tuntematon komento ja kysytään syötettä uudestaan
def user_command(commands):
    user_input = None
    while user_input not in commands:
        user_input = input("Syötä seuraava liike: ").lower()
        if user_input not in commands:
            print("Tuntematon komento")
    return user_input



# Funktio tulostaa kaikki saatavilla olevat kohteet
def user_search(countries):
    print("\n SAATAVILLA OLEVAT KOHTEET")
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








