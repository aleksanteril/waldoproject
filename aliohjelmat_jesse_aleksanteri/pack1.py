



def vihje(clue):
    print(clue)
    return


















################### Tähän alapuolelle JESSEN funktiot, yläpuolelle ALEKSANTERIN

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





























