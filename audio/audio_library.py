# Tuodaan playsound versio 1.2.2
from playsound import playsound

# Funktio joka soittaa ääniä valutin sound_num parametrin mukaan
def play_game_sound(sound_num):
    if sound_num == 1:
        playsound("clue_sound.mp3")
    elif sound_num == 2:
        playsound("help_command.mp3")
    elif sound_num == 3:
        playsound("radio_sound.mp3")
    elif sound_num == 4:
        playsound("right_country.mp3")
    elif sound_num == 5:
        playsound("travel_sound.mp3")
    elif sound_num == 6:
        playsound("game_start.mp3")
    elif sound_num == 7:
        playsound("command_sound.mp3")
    elif sound_num == 8:
        playsound("simply_the_best.mp3")
    return

# Erillinen funktio waldon äänille
def play_waldo_sound(sound_num):
    if sound_num == 1:
        playsound("w_excuse_me.mp3")
    elif sound_num == 2:
        playsound("w_help_me.mp3")
    elif sound_num == 3:
        playsound("w_huuh.mp3")
    elif sound_num == 4:
        playsound("w_lets_get_going.mp3")
    elif sound_num == 5:
        playsound("w_list_of_countries.mp3")
    elif sound_num == 6:
        playsound("w_mmm_bad_luck.mp3")
    elif sound_num == 7:
        playsound("w_rings_a_bell.mp3")
    elif sound_num == 8:
        playsound("w_signals_the_same.mp3")
    elif sound_num == 9:
        playsound("w_splendid.mp3")
    elif sound_num == 10:
        playsound("w_top_of_the_morning.mp3")
    elif sound_num == 11:
        playsound("w_we_getting_closer.mp3")
    elif sound_num == 12:
        playsound("w_what_r_u_leaving_me.mp3")
    elif sound_num == 13:
        playsound("w_where_to_next.mp3")
    elif sound_num == 14:
        playsound("w_youre_hysterical.mp3")
    return



