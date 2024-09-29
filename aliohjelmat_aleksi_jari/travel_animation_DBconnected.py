import os
import time
import pyfiglet
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


#   VAIHTOEHDOT HAKEE % PALAUTTAA
def eu_countries():
    query_eu = "SELECT name FROM country WHERE continent = 'EU';"
    cursor = yhteys.cursor()
    cursor.execute(query_eu)
    eu_countries = cursor.fetchall()
    eu_countries = [row[0] for row in eu_countries]
    return eu_countries

# VALINTA
def country():
    eu_lista= eu_countries()
    print ("(EU countries)")
    print(",".join(eu_lista))
    while True:
        valinta = input("Where would you like to travel?: ").capitalize()
        if valinta in eu_lista:
            return valinta
        else:
            print("Virhe tai ei ole EU maa. ")


# VIESTI
def message(country_prittified):
    ascii_art = pyfiglet.figlet_format(f"ARRIVING TO: {country_prittified}... .. .")
    print(ascii_art)
    time.sleep(5)

# funktiopäivittää ruutua
def clear_screen():
    # print("1h later...")
    os.system('cls' if os.name == 'nt' else 'clear')


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
        time.sleep(0.9)


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
        time.sleep(3.0)


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






eu_maa_lista = eu_countries()
selected_country = country()

travel()
clear_screen()
flying()

clear_screen()
message(selected_country)

landing()
clear_screen()
runway()

