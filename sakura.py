import sys
import colorama

COMMANDS = {"kill" : "Stop"}

def main(argv: list[str]) -> None:
    print(\
"\033[H\033[J"+rf"""{colorama.Style.BRIGHT}           _                    
          | |                   
 ___  __ _| | ___   _ _ __ __ _ 
/ __|/ _` | |/ / | | | '__/ _` |
\__ \ (_| |   <| |_| | | | (_| |
|___/\__,_|_|\_\\__,_|_|  \__,_|{colorama.Style.NORMAL} botnet
""")
    while 1:
        command = input(f"botnet{colorama.Style.DIM}@sakura{colorama.Style.NORMAL} $ ")

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("\033[H\033[J\n")