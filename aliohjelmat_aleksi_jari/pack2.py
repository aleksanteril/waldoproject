
import random

# ottaa listan ja arpoo jonkun arvon listasta
def case_randomizer(list):
    random_index = random.randint(0, len(list)-1)
    random_str = list[random_index]
    return random_str[0]


#Kysytään käyttäjän nimi, ja palautetaan se tarkistuksia varten
def input_username():
    username = input("\nWaldo greets you! Hello my friend: ").lower()
    return username


#tulostaa komennot käyttäjälle
def help():
    print("Using command 'help' opens the help window.")
    print("Using command 'clue' gives you a clue.")
    print("Using command 'destinations' prints the country's you can travel to.")
    print("Using command 'travel' travels you to your country of choosing.")
    print("Using command 'radio' displays signal strength for the location of Waldo's case")
    return

