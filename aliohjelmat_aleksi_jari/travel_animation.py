import os
import time


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
        time.sleep(2.5)


def landing():
    frames = [
        """
        """,
        """ 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        """,
        """                                                                                                      --@--@--
 
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
        time.sleep(0.5)


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
        time.sleep(0.5)


takingoff()
flying()

clear_screen()

time.sleep(0.5)

landing()

clear_screen()
time.sleep(0.5)
runway()