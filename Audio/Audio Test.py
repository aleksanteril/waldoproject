# Tuodaan playsound versio 1.2.2
from playsound import playsound

# Funktio joka soittaa ääniä valutin sound_num parametrin mukaan
def play_sound(sound_num):
    if sound_num == 1:
        playsound("clue_sound.mp3")
        print("TOIMIIKO")
    if sound_num == 2:
        playsound("help_command.mp3")
        print("perkele")
    if sound_num == 3:
        playsound("radio_sound.mp3")
        print("asdasda")
    if sound_num == 4:
        playsound("right_country.mp3")
        print("Asdasd")
    if sound_num == 5:
        playsound("travel_sound.mp3")
    if sound_num == 6:
        playsound("game_start.mp3")
    if sound_num == 7:
        playsound("-.mp3")
    if sound_num == 8:
        playsound("-.mp3")
    if sound_num == 9:
        playsound("-.mp3")
    if sound_num == 10:
        playsound("-.mp3")
    return

# Kutsuu funktiota parametrilla
print("kgfkjgfjkgkfjkdsksfd")
play_sound(2)