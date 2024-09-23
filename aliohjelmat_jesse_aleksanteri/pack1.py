



def country_clue(clue):
    for clue in clue:
        print(clue[0])
    return


















################### Tähän alapuolelle JESSEN funktiot, yläpuolelle ALEKSANTERIN

# Funktio ottaa käyttäjän syötteen ja vertaa sitä monikkoon jos,
# komento löytyy monikosta niin palauttaa syötteen
def user_command():
    commands = ("vihje", "hae", "matkusta", "tracker", "lämpötila", "maat", "help")
    user_input = None
    while True:
        user_input = input("Syötä seuraava liike: ").lower()
        if user_input in commands:
            break
        else:
            print("Tuntematon komento")
    return user_input




























