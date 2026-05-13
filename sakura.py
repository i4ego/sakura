import sys, os
import colorama
import termcursor
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import Suggestion, ThreadedAutoSuggest, AutoSuggest
from prompt_toolkit.key_binding import KeyBindings

COMMANDS = {"kill": ("Stop all workers", "Usage:\n\tkill\n\tstop"),
             "ddos":("Start ddos attack", "Usage:\n\tddos udp example.com 443\t || DDOS example.com:443\n\tddos udp example.com 443 15\t || DDOS example.com:443 (15 workers)"), 
             "help":("Show help", "Usage:\n\thelp"),
             "synflood":("Start SYNFlood", "Usage:\n\tpython3 sakura.py SYNFLOOD example.com || SYNFlood example.com"), 
             "exit":("Exit from sakura terminal", "Usage:\n\texit"),
             "restart":("Restart sakura terminal", "Usage:\n\trestart")}
SECONDARY_COMMANDS = {"ddos":("udp", "tcp", "get", "head", "post", "website")}
class ListAutoSuggest(AutoSuggest):
    def get_suggestion(self, buffer, document):
        text = document.text
        if len(text.split(" ")) == 2:
            for scmd in list(SECONDARY_COMMANDS):
                for rscmd in SECONDARY_COMMANDS[scmd]:
                    if rscmd.startswith(text.strip().split(" ")[1]) and rscmd != text.split(" ")[1].strip():
                        return Suggestion(rscmd[len(text):])
        for cmd in list(COMMANDS):
            if cmd.startswith(text) and cmd != text:
                return Suggestion(cmd[len(text):])
        return None

kb = KeyBindings()
session = PromptSession(
    auto_suggest=ThreadedAutoSuggest(ListAutoSuggest()),
    key_bindings=kb,
)

SERVER = ""
PORT = 0
PASSWORD = ""

### -=-=-=- BINDINGS -=-=-=- ###

def on_exit():
    print(colorama.Style.RESET_ALL)
    print("\033[H\033[J\n")
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
    match f[0]:
        case "help":
            for command in COMMANDS:
                print(f"{command}{(9-len(command))*" "} | {COMMANDS[command][0]}")
        case "kill":
            print(".. under construction ..")
        case "ddos":
            print(".. under construction ..")
        case "synflood":
            print(".. under construction ..")
        case "status":
            print(".. under construction ..")
        case "proxy":
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
    except KeyboardInterrupt:
        on_exit()