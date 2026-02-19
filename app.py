import time
import sys
import os
import termios
import shutil
import textwrap

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

fd = sys.stdin.fileno()
original_settings = termios.tcgetattr(fd)

def wrap_text(text):
    width = shutil.get_terminal_size((80, 20)).columns
    return textwrap.fill(text, width=width)

def disable_input():
    new_settings = termios.tcgetattr(fd)
    new_settings[3] &= ~termios.ECHO
    new_settings[3] &= ~termios.ICANON
    termios.tcsetattr(fd, termios.TCSADRAIN, new_settings)

def enable_input():
    termios.tcsetattr(fd, termios.TCSADRAIN, original_settings)

disable_input()

def veilige_input(prompt="", color=GREEN):
    enable_input()

    termios.tcflush(fd, termios.TCIFLUSH)

    try:
        if color:
            sys.stdout.write(color)
            sys.stdout.flush()
        return input(prompt)
    finally:
        if color:
            sys.stdout.write(RESET)
            sys.stdout.flush()
        disable_input()

def clear_screen():
    os.system("clear")

def typewriter(text, delay=0.05, color=GREEN):
    text = wrap_text(text)

    if color:
        sys.stdout.write(color)

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    if color:
        sys.stdout.write(RESET)

    print()


def mooie_progress_bar():
    stappen = 50
    bar_lengte = 30
    sys.stdout.write(GREEN)
    print("Laden: ", end='', flush=True)

    for i in range(stappen + 1):
        percent = (i / stappen) * 100
        blokjes = i * bar_lengte // stappen
        bar = '█' * blokjes + '░' * (bar_lengte - blokjes)
        print(f'\r[{bar}] {percent:.1f}%', end='', flush=True)
        time.sleep(0.1)

    sys.stdout.write(RESET)
    print("\n")

clear_screen()

while True:
    time.sleep(0.8)
    clear_screen()
    typewriter("Wachtwoord:", 0.07)
    wachtwoord = veilige_input("> ")
    mooie_progress_bar()

    if wachtwoord == "120122":
        clear_screen()
        typewriter("Wachtwoord is gevalideerd!\n")
        break
    else:
        typewriter("Onjuist wachtwoord!\n", color=RED)

vragen = [
    {
        "vraag": "Vraag 1: Hoeveel meer radioactieve straling was er bij de superwolven dan wat volgens de menselijke veiligheidslimiet mag?",
        "antwoorden": ["6 keer", "6", "zes keer", "zes"],
        "hint": "Het is een enkel cijfer, en best een klein getal."
    },
    {
        "vraag": "Vraag 2: Hoeveel ton woog de deksel die werd weggeblazen door de stoomexplosie?",
        "antwoorden": ["1000 ton", "1000ton", "duizend ton", "1000"],
        "hint": "Het is in tonnen uitgedrukt, niet in kilo's."
    },
    {
        "vraag": "Vraag 3: Welke naburige stad werd ook getroffen door de explosie van Tsjernobyl?",
        "antwoorden": ["pripjat", "pripyat"],
        "hint": "De stad ligt op korte afstand van de kerncentrale."
    },
    {
        "vraag": "Vraag 4: Hoe groot was de vervreemdingszone rond de kerncentrale?",
        "antwoorden": ["30 km", "30km", "dertig km", "30 kilometer"],
        "hint": "Het aantal is kleiner dan 50, een mooi rond getal."
    },
    {
        "vraag": "Vraag 5: Zoek de letters met de blacklight en vorm een woord",
        "antwoorden": ["uranium"],
        "hint": "De vierde letter is n."
    },
]

def vraag_stel(vraag, antwoorden, hint):
    fouten = 0
    typewriter(vraag)
    antwoorden = [a.lower() for a in antwoorden]

    while True:
        respons = veilige_input("Antwoord: ").strip().lower()

        if respons in antwoorden:
            clear_screen()
            typewriter("Correct!")
            return
        else:
            fouten += 1
            typewriter("Fout antwoord!", color=RED)

            if fouten == 3:
                typewriter(f"Hint: {hint}")

def main():
    for v in vragen:
        vraag_stel(v["vraag"], v["antwoorden"], v["hint"])

    time.sleep(1)
    clear_screen()
    typewriter("Alle vragen beantwoord")
    typewriter("Wachtwoord is 9128")
    time.sleep(15000)

    enable_input()  # restore terminal before exit


main()
