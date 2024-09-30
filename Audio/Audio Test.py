# Tuodaan playsound versio 1.2.2
from playsound import playsound

# Funktio joka soittaa ääniä valutin sound_num parametrin mukaan
def play_game_sound(sound_num):
    if sound_num == 1:
        playsound("clue_sound.mp3")
        print("TOIMIIKO")
    elif sound_num == 2:
        playsound("help_command.mp3")
        print("perkele")
    elif sound_num == 3:
        playsound("radio_sound.mp3")
        print("asdasda")
    elif sound_num == 4:
        playsound("right_country.mp3")
        print("Asdasd")
    elif sound_num == 5:
        playsound("travel_sound.mp3")
    elif sound_num == 6:
        playsound("game_start.mp3")
    elif sound_num == 7:
        playsound("command_sound.mp3")
    elif sound_num == 8:
        playsound("simply_the_best.mp4")
    return

# Kutsuu funktiota parametrilla
print("kgfkjgfjkgkfjkdsksfd")
play_game_sound(2)

def play_waldo_sound(sound_num):
    if sound_num == 1:
        playsound(".mp3")
    elif sound_num == 2:
        playsound(".mp3")
    elif sound_num == 3:
        playsound(".mp3")
    elif sound_num == 4:
        playsound(".mp3")
    elif sound_num == 5:
        playsound(".mp3")
    elif sound_num == 6:
        playsound(".mp3")
    elif sound_num == 7:
        playsound(".mp4")
    elif sound_num == 8:
        playsound(".mp3")
    elif sound_num == 9:
        playsound(".mp3")
    elif sound_num == 10:
        playsound(".mp3")
    elif sound_num == 11:
        playsound(".mp3")
    elif sound_num == 12:
        playsound(".mp3")
    elif sound_num == 13:
        playsound(".mp3")
    elif sound_num == 14:
        playsound(".mp3")
    return


play_waldo_sound(1)


