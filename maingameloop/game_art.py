#GAME INTRO
import time

def waldo_animated():
    art = [
        "      \033[91m         *#&@&&.  \033[0m                                                      ",
        "      \033[91m          &((/@    &%/      \033[0m                  #(&&&# .        ",
        "      \033[91m          &/((@  #//(/.   %//&/&#.       \033[0m              /&&&/(       ",
        "      \033[91m          (/(/& %/%/((&  (/%  @///&    &/#&&    \033[0m                    (&&@#      ",
        "      \033[91m          //(&(/%((/(&%(/&  ./(/(    ./(//   //(////#&  . \033[0m                    &&&#@   ",
        "      \033[91m           ((//&   (((((#    &/((////(//((&  @/(/&   ** .////(//(&       \033[0m                 *#&@&&. ",
        "      \033[91m           &&#@    %(//&    #(/(#    //((#  ./((//#&@@  &(((% ./(/#   @/((//#&&/        \033[0m           #",
        "      \033[91m                           %(((&    &/(/%  &///@  *&  #/((#&&/((/&   /(//   *& #/(& &(///#@   \033[0m    &#",
        "    \033[92m       %###%    %%&&                \033[91m @//((  (//((       &(((&//(&     @/((#&&%(  &%% /(/#  #/%  \033[0m   &.#",
        "    \033[92m        ###%  #####@   @##&   .@//           \033[91m #%@%//#  (//(% &/(/&   ./(((  #@&      /(((/&    \033[0m   %/#.",
        "    \033[92m        %### &#####%  %##    &###&      &&&(#         \033[91m    #@  %/((&  &/(/&            *%(((/#  \033[0m   &# ",
        "    \033[92m        &#####& %####(#@   %(####(      %###(     %%&%/           \033[91m  ##&&#///%     @(&   &/((  \033[0m  #(#  ",
        "    \033[92m        &###%   &#####.   %#& &###&    %###&      /###%%&###&                     \033[91m  &(/////&  \033[0m   &#   ",
        "    \033[92m       **/&&    %###&   &##(&&%###%    ####.      %###/   &###%   &########%(                 %*#   ",
        "     \033[92m                    @%#&     %###(   &###&       ####&    &###& &###%     &###(  ##  /(& &(///&#.   ",
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


        "        . *        &#%.   ((&%          ",
        "   *,, . ,    ., %*  &###&#&%&#%        ",
        " ..&(...,/%%   . @##(%(####&#%#%.       ",
        "  . .,..,, .    . /#&%%(.&  .&% .       ",
        "  .   /%(        , @/  .,/,(.,          ",
        "  . #%(/(         . %(.%%%,.&           ",
        "  ,//###            . ,...,.            ",
        "  .&%(..             ., .,,             ",
        " . %#### \033[31m          &###########(,                  \033[0m",
        "\033[31m . * (##  ###  ###             ..*#(.              \033[0m",
        "\033[31m  , ###  ,###  .#####################&             \033[0m",
        "\033[31m                 *                    #            \033[0m",
        "\033[31m                . %####################&           \033[0m",
        "\033[31m                . %###/(..         #    /          ",
        "\033[31m                   & ########%#####  /    /    \033[0m",
        "\033[31m                 .,###############/#  /   /          \033[0m",
        "\033[31m                 . #################  ##(/#      \033[0m",
        "\033[31m                   /                / /  ,#    \033[0m",
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

        "\033[33m                                                                                    ",
        "                                                                                           ",
        "                                                                                       ",

    ]

    for waldo in art:
        print(waldo)
        time.sleep(0.1)

waldo_animated()