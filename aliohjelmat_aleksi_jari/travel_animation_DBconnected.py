import os
import time
import pyfiglet  # TÄMÄ KIRJASTO LISÄTTÄVÄ
import mysql.connector

# VÄLIAIKAISESTI KOODISSA
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='megapint',
    password='wine',
    autocommit=True
)


# ALEKSANTERIN KOODI
def travel(username, country_list):
    user_country = "finland"
    while True:
        player_input = input("\nWaldo is excited! Where do you want to travel?: ").lower()
        if player_input == "destinations":
            print(country_list)
        elif player_input == user_country:
            print("Waldo is confused, we are here already! What do you mean?")
        elif player_input not in country_list:
            print("Waldo is confused, what do you mean?")
            print("Type 'destinations' to see Waldo's list of countries.")
        else:
            break
    return player_input


# PRINTTAA SAAPUMISMAAN
def display_ascii_welcome(city_name):
    ascii_text = pyfiglet.figlet_format(f"Welcome to {city_name}")
    return ascii_text


# funktiopäivittää ruutua
def clear_screen():
    # print("1h later...")
    os.system('cls' if os.name == 'nt' else 'clear')


def takingoff():
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
        time.sleep(0.6)


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
        time.sleep(2.0)


def landing(city_name):
    welcome_message = display_ascii_welcome(city_name)
    frames = [
        """
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        """,
        """
        """,
        f"""
       {welcome_message}
       """,

        """ 
        """,
        """                                                                                                      --@--@--
 
        """,
        """                                                                                           --@--@--
 
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
    ]
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.4)


def runway():
    frames = [
        """
                                                          ___
                                                         |   |
                                                         |   |
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
                                                         |   |
                                                         |   |
                                                         |___|
        """,

    ]

    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.4)


def main_game(username, country_list):
    destination = travel(username, country_list)

    takingoff()
    flying()

    clear_screen()

    landing(destination)

    clear_screen()
    time.sleep(0.5)
    runway()


country_list = ["germany", "france", "italy", "spain"]

main_game("waldo", country_list)