import keyboard
import os
import mouse
import threading
import time

if os.name == 'nt':
    os.system('')
    
def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    logo = """
                    \033[38;5;196m (       )     )       (       )    )  \033[0m
                    \033[38;5;202m )\ ) ( /(  ( /(  *   ))\ ) ( /( ( /(  \033[0m
                    \033[38;5;202m(()/( )\()) )\()` )  /(()/( )\()))\()) \033[0m
                    \033[38;5;208m /(_)((_)\ ((_)\ ( )(_)/(_)((_)\((_)\  \033[0m
                    \033[38;5;208m(_))   ((_)  ((_(_(_()(_))  _((___((_) \033[0m
                    \033[38;5;214m| _ \ / _ \ / _ |_   _/ __|| || \ \/ / \033[0m
                    \033[38;5;214m|   /| (_) | (_) || | \__ \| __ |>  <  \033[0m
                    \033[38;5;220m|_|_\ \___/ \___/ |_| |___/|_||_/_/\_\ \033[0m

                                   \033[38;5;220mSPAMDANCE\033[0m
                          \033[38;5;220mgithub.com/rootshx/spamdance\033[0m

"""
    Clear()
    print(logo)

if __name__ == "__main__":
    main()

spamming = False

def spam_dance():
    global spamming
    while spamming:
        keyboard.send('ctrl+3')
        time.sleep(0.2)

def start_spam():
    global spamming
    if not spamming:
        spamming = True
        threading.Thread(target=spam_dance, daemon=True).start()

def stop_spam(event=None):
    global spamming
    spamming = False

mouse.on_button(start_spam, buttons=('x2'), types=('down',))

keyboard.on_press(lambda e: stop_spam() if e.name != 'space' else None)
mouse.on_button(stop_spam, buttons=('right'), types=('down',))

keyboard.wait('.')