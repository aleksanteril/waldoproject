




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



#Kuuma/kylmä mekaniikka joka vertaa edellistä etäisyyttä metreissä
def hot_cold_mechanic(user_distance_to_case):
    distance_meters = user_distance_to_case[0]
    print(distance_meters[0])



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









