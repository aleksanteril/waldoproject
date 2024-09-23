


#Funktio tulostaa vihjeen listasta, joka tulee sql kyselyn kautta
def country_clue(clue):
    for clue in clue:
        print(clue[0])
    return


















################### Tähän alapuolelle JESSEN funktiot, yläpuolelle ALEKSANTERIN

def user_command(commands):
    user_input = None
    while True:
        user_input = input("Syötä seuraava liike: ").lower()
        if user_input in commands:
            break
        else:
            print("Tuntematon komento")
    return user_input




























