
import random


def case_randomizer(list):
    random_index = random.randint(0, len(list)-1)
    random_str = list[random_index]
    return random_str[0]

def start_game():
    print("PRINT TAUSTATARINA TJPS")
   #print("PRINT TARKOITUS esim. Löydä matkalaukku niin ja näin.")
    #print("PRINT OHJEISTUS MITEN MATKUSTAA / SIIRTYY / komennot")
    #print("PRINT KIRJOITA sana ICAO -> Kirjoita maan -> saat vastauksena sen pääkentän ICAO:n ")
    username = input("SYÖTÄ PELAAJAN NIMI: ")
    return username

def help(commands):
    print(commands)
    return