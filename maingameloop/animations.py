##GAME INTRO
import time
import pyfiglet

def waldo_animated():
    art = [
        "      \033[91m         *#&@&&.  \033[0m                                                      ",
        "      \033[91m          &((/@    &%/      \033[0m                  #(&&&# .        ",
        "      \033[91m          &/((@  #//(/.   %//&/&#.       \033[0m              /&&&/(       ",
        "      \033[91m          (/(/& %/%/((&  (/%  @///&    &/#&&    \033[0m                    (&&@#      ",
        "      \033[91m           //(&(/%((/(&%(/&  ./(/(    ./(//   //(////#&  . \033[0m                    &&&#@   ",
        "      \033[91m           ((//&   (((((#    &/((////(//((&  @/(/&      .////(//(&       \033[0m                 *#&@&&. ",
        "      \033[91m           &&#@    %(//&    #(/(#    //((#  ./((//#&@@  &(((% ./(/#   @/((//#&&/        \033[0m           #",
        "      \033[91m                           %(((&    &/(/%   ///@       /((#&&/((/&   /(//        #/(&&(///#@   \033[0m    &#",
        "    \033[92m         ##%                         \033[91m @//(   ##/((       &(((&//(&     @/((#&&%(   &%%/(/#  #/%  \033[0m   &.#",
        "    \033[92m        ###%  #####@   @##&   .@//          \033[91m #%@%//#€   /(% &/(/&   ./(((           /(((/&    \033[0m   %/#.",
        "    \033[92m        %### &#####%  %##    &###&      &&&(#         \033[91m  ###@  %/((&  &/(/             *%(((/#  \033[0m   &# ",
        "    \033[92m        &#####& %####(#@   %(####(      %###(     %%&%/           \033[91m  ##&&#///%     @(&   &/((  \033[0m  #(#  ",
        "    \033[92m        &###%   &#####.   %#& &###&    %###&      /###%%&###&                     \033[91m  &(/////&  \033[0m   &#   ",
        "    \033[92m       **/&&    %###&   &##(&&%###%    ####.      %###/   &###%   &########%(               \033[97m  %*#\033[0m   ",
        "     \033[92m                    @%#&     %###(   &###&       ####&    &###& &###%     &###(  ##  /(& &(/// &#.   ",
        "     \033[92m                              #&&&  .#####%@&&   %####   &#### (####      ####%   #  /(/#    #/% \033[0m&.#",
        "     \033[92m                                                 &#####%#####  (###%      %###@       /(((/&    \033[0m#. ",
        "     \033[92m                                                                ####@   /####&         *%(((/#  \033[0m&#",
        "     \033[92m                                                                   (&#####&.       @(&   &/((   \033[0m.&#",
        "     \033[92m                                                                                    &(/////&     \033[0m ",
        "     \033[92m                                                                                   \033[0m         ",
        "     \033[37m                                               @@@@@             \033[0m        _    __        ",
        "     \033[37m                                       @@@@@@@@@@@@@@@@@@@@@@    \033[0m       (_) _(__)_      ",
        "     \033[37m                                     @@   @@  @     @@  @@   @@  \033[0m       (_)(_)  (_)     ",
        "     \033[37m                                     @@@@@@@  @@@@@@@@  @@@@@@@  \033[0m       (_)    (_)      ",
        "     \033[37m                                     @@@@@@@  @@@@@@@@  @@@@@@@  \033[0m       (_)   (_)       ",
        "     \033[37m                                     @@@@@@@  @@@@@@@@  @@@@@@@  \033[0m        _     _        ",
        "     \033[37m                                       @@@@@@@@@@@@@@@@@@@@@@    \033[0m       (_)   (_)       ",


        "        . *  \033[36m      &#%.   ((&%    \033[0m      ",
        "   *,, . ,   \033[36m ., %*  &###&#&%&#%  \033[0m      ",
        " ..&(...,/%% \033[36m  . @##(%(####&#%#%. \033[0m      ",
        "  . .,..,, .    . /#&%%(.&  .&% .       ",
        "  .   /%(        , @/  .,/,(.,          ",
        "  . #%(/(         . %(.%%%,.&           ",
        "  ,//###            . ,...,.            ",
        "  .&%(..             ., .,,             ",
        " . %#### \033[31m          &###########(,                  \033[0m",
        "\033[31m . * (##@€###  \033[0m\033[97m ###########%##..*#(.              \033[0m",
        "\033[31m  , ###  ,###  .#####################&             \033[0m",
        "\033[97m                 *##############%###\033[0m\033[31m   \         \033[0m",
        "\033[31m                . %##################|   \       \033[0m",
        "\033[97m                . %###/(..########%#\033[0m\033[31m |   /  \033[0m",
        "\033[31m                   & ########%#####  /    /    \033[0m",
        "\033[97m                 .,###############/#\033[0m\033[31m  /   /          \033[0m",
        "\033[31m                 . #################  ##(/#      \033[0m",
        "\033[97m                   /###############/\033[0m\033[31m /  ,#    \033[0m",
        "\033[33m                  ,.(/((#(((/(((((((, ,####,      \033[0m",
        "\033[36m                  . ((((#((&/(((((((&\033[0m     \033[31m    \033[0m",
        "\033[36m                  . %((#((((((((((#&&\033[0m   \033[31m   \033[0m",
        "\033[36m                   .%(((((((&%((((((/\033[0m  \033[31m  \033[0m",
        "\033[36m                   .*(((((((%(((((((/\033[0m  \033[31m          \033[0m   ",
        "\033[36m                   . /((((((((((((((( \033[0m   \033[31m           \033[0m",
        "\033[36m                   ..%(((((((@((((((( \033[0m                   \033[0m   ",
        "\033[36m                    .,(((((((&((((((( \033[0m                   \033[0m   " ,
        "\033[36m                    . (((((((@(((((((., \033[0m                 \033[0m   ",
        "\033[36m                    . %((((((#/(((((((%  \033[0m                \033[0m   ",
        "\033[36m                      . ((((((#/((((((                   \033[0m          ",
        "\033[36m                      . (((((((#((((((                   \033[0m          ",
        "\033[36m                       ,%((((((%(((((( *                 \033[0m          ",
        "\033[36m                       . ((((((&((((((,/                 \033[0m          ",
        "\033[36m                       . ((((((&((((((*                  \033[0m          ",
        "\033[31m                        *%((((##%(((((((((               \033[0m          ",
        "\033[31m                    . ((((((/&(/#((((/((((#              \033[0m",

        "\033[33m                                                                                  \033[0m",
        "                                                                                           ",
        "                                                                                       ",

    ]

    for waldo in art:
        print(waldo)
        time.sleep(0.1)


# VIESTI
def message(country_prittified):
    ascii_art = pyfiglet.figlet_format(f"ARRIVING TO: {country_prittified}... .. .")
    print(ascii_art)


# funktiopäivittää ruutua
def clear_screen():
    print('\n' * 50)


def travel():
    frames = [
        """
        """,
        """

                                                          ###                                       
                                                       #######                                      
                                                       # ### ##                                     
                                                      #### ####                                     
                                                      ###   ###                                     
                                                      ###   ####                                    
                                                     ####    ###                                    
                                                     ###     # #                                    
                                                     ###     # #                                    
                                                     # #     # #                                    
                                                     ###     # #                                    
                                                     ###     # #                                    
                                                     ###     # #                                    
                                                             # #                                      
                                                     ###     # #
                                              ###    ###     # #      ###                             
                                            ######   ###  ######   #### #                             
                                            # ####   ###  ######   ######                             
                                           ####### ### ### #####   ### ###                            
                                           ### ##### ######     #### #####                            
                                           ###### #### ## #    ####  #####                            
                                        ######  #### # ## #    ########### ###                        
                                       ##############   # ## #          ##### # #####
                               ### # #### ###          # ## # ### #  ####   #### #### # ###             
                         ##### #####   #######   ### ###### ###################   ##### ####          
                       ############### # #####  ## # ## ### # ###  ##### #######  ######## ####       
                       # ##########  # # ##### ##### ###### ################## # ######  #### #       
                       ##### ### ##### ####    ####  ###### ### #  #####  ###### ###### ########      
                       ## ## #### #    ####    ####  ###### #####         ###    ###### #### # #      
                       #####    ###     ###          ###### ### #                 ####  #### ###      
        """,  ###### ### #
        """                                                    # ## # # ###                                     
                                                     # ## # ###                                       
                                                     # ## # ####                                      
                                                     # ## #  ###                                      
                                                     # ## #### #                                      
                                                     # ## #### #                                      
                                                     # ## ##   #                                      
                                                     #### ######                                      
                                                     #### ######                                      
                                                      # # # #                                         
        """,
        """                                                     #########                                       
                                                  ####### ######                                     
                                                # # ########## ####                                  
                                              ##  #### # ### #### ###                                
                                            ### #### # # # ### ###  ###                              
                                           ###### ## ### ##### #########                             
                                           #### #### ########  #### ####                             
                                           ###        ### ###        ###                             
                                                      #######                                        
                                                      # # # #                                        
                                                      # # ###                                        

         """,
    ]

    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.5)


def flying():
    frames = [
        """
        """,
        """  

                                                                                     @@@@%
                                                                                 @@@@@@@@@
                                      @@%.           :@.                     .@@@@@@@@@@*
                                     =@@@@@@@@@-.   .@@@@@.      .          .@@@@@@@@@@@@
                                       @@@@@@@@@@@@@@@@@@.    @@@@.      .@@@@@@@@@@@@@                   
                                            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@.
                             .@@@@@         .@@@@@@@@@@@@@@@@@@@@@.. .@@@@@@@@@@@@@@.                     
                             .@@@+              .@@@@@@@+@@@@@@@@@@@@@@@@@@@@@@*#@@@.                      
                           .@@@@       -@@@        %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                        
                          @@@@        @@@@.           @@@@@@@@@@@@@@@@@@@@@@@@@@                           
                        .@@@       .@@@@.               .@@@@@@@@@@@@@@@@@@@@@                             
                   .@@#        .@@@                     @@@@@@@@@@@@@@@@@@@ ..
                     *+:        .@@@.                       :@@@@@@@+@@@@@@@@@@@@@                         
                   .@.         @@@                         @@@@@@@@@@@@@@@@@@@@@@@@                        
                  @.         .@@.                        @@@@@@@@@@@@@@@@@@@@@@@@@                         
                :.          @@                         .@@@@@@@@@@@@@@@@@@@@@@@@                           
              ..         .@@.                         @@@@@@@@@@@@@ @@@@@@@@@@@@                           
                                                    ###############################
                    .#           #@@+..          @@+@++++@+@         =@@@@@@@@%@@@@@                     
                    %           .@@@@@@@@@@+.   .@@@@@@@@@@.           .@@@@@@@@@@@@.
                   ..               .@@@@@@@@@@@@@@@@@@@@@.              .@@@@@@@@@.                       
                                       .@@@@@@@@@@@@@@@@                   @@@@@@@@                        
                                          .@@@@@@@@@@#                      @@@@@@@.                       
                                            @+@@@@@@@@                       @@@@@@@                       
                                          .@@@@@@@@@@@.                       .@@@@@                       
                                         .@@@@  +@@@@@@                 ...     @@@@@                      
                                         @.      .@@@@@               .@@@@.     @@@@.                     
                                                .@@@@@             .@@@@        @@@@                     
                                                 .@@@@.          .@@@@           -@.
                                                      @         .@@@.      .@@@@                           
                                                              .@@@       . @@@@                            
                                                             %@@        .@@@@                              
                                                           .@@        .@@@@                                
                                                         .@@         .@@@                                  
                                                        ##         .@@%                                                                                                                      
        """,

    ]
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(1.0)



def landing():
    frames = [
        """


















                                                                               --@--@--
        """,
        """
                                                                             --@--@--
        """,
        """                                                                                            
                                                                           --@--@--
        """,
        """                                                                                           
                                                                          --@--@--
        """,
        """
                                                                         --@--@--
        """,
        """
                                                                     --@--@--
        """,
        """
                                                                  --@--@--
        """,
        """
                                                               --@--@--
        """,
        """
                                                          --@--@--
        """
    ]
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.7)


def runway():
    frames = [
        """
                                                          ___
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |___|
        """,
        """

             ✈


                                                          ___
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |___|
        """,
        """

             ✈


                                                          ___
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |___|
        """,
        """

             ✈


                                                          ___
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |___|
        """,
        """
              ✈


                                                          ___
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |__ |
        """,
        """
               ✈


                                                          ___
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |   |
                                                         |___|
        """,

    ]

    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.8)


# Animaatio kutsu, koko animaation sykli
def start_travel_animation(country_name):
    travel()
    clear_screen()
    flying()

    clear_screen()
    message(country_name)
    return

# Tulostaa voitto tekstin
def print_congratulations(message):
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(0.1)
    print()


# Tulostaa loppuun statsit hienommin (pyfligtet)
def display_results(total_kilometers, travel_counter):
    ascii_art = pyfiglet.figlet_format("GAME RESULTS")
    print(ascii_art)
    border = "=" * 50
    print(border)

    print(f"{'Kilometers travelled:':<30} {total_kilometers:.0f} km")
    print(f"{'Flights taken:':<30} {travel_counter}")
    print(f"{'Your CO2 footprint:':<30} {total_kilometers * 8:.0f} kg  🌱")
    print(border)
    print()
