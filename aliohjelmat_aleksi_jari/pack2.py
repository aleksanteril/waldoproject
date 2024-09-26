
import random

# ottaa listan ja arpoo jonkun arvon listasta
def case_randomizer(list):
    random_index = random.randint(0, len(list)-1)
    random_str = list[random_index]
    return random_str[0]


#pelinalustus + Jesse kirjoita tarina
def start_game():
    username = input("Syötä pelaajan nimi: ").lower()
    return username


#tulostaa komennot käyttäjälle
def help(commands):
    print(commands)
    return