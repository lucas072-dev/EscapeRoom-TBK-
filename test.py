import time
import sys
import os

# ===== KLEUR =====
RED = "\033[91m"
RESET = "\033[0m"

# ===== INPUT LOCK =====
input_toegestaan = True

def veilige_input(prompt=""):
    while not input_toegestaan:
        time.sleep(0.05)
    return input(prompt)

# ===== CLEAR SCREEN =====
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ===== TYPEWRITER =====
def typewriter(text, delay=0.05, color=None):
    global input_toegestaan
    input_toegestaan = False

    if color:
        sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if color:
        sys.stdout.write(RESET)
    print()

    input_toegestaan = True

# ===== LOADING BAR =====
def mooie_progress_bar():
    global input_toegestaan
    input_toegestaan = False

    stappen = 50
    bar_lengte = 30
    print("Laden: ", end='', flush=True)

    for i in range(stappen + 1):
        percent = (i / stappen) * 100
        blokjes = i * bar_lengte // stappen
        bar = '█' * blokjes + '░' * (bar_lengte - blokjes)
        print(f'\r[{bar}] {percent:.1f}%', end='', flush=True)
        time.sleep(0.1)

    print("\nGevalideerd")
    input_toegestaan = True

# ===== START =====
clear_screen()

# ===== START WACHTWOORD =====
while True:
    typewriter("Wachtwoord:", 0.07)
    wachtwoord = veilige_input("> ")
    mooie_progress_bar()

    if wachtwoord == "1908":
        clear_screen()
        typewriter("Het wachtwoord is correct!\n")
        break
    else:
        typewriter("Onjuist wachtwoord.\n", color=RED)

# ===== VRAGEN =====
vragen = [
    {
        "vraag": "Vraag 1: Hoeveel meer radioactieve straling was er bij de superwolven dan wat volgens de menselijke veiligheidslimiet mag?",
        "antwoorden": ["6 keer", "6", "zes keer"],
        "hint": "Het is een enkel cijfer, en best een klein getal."
    },
    {
        "vraag": "Vraag 2: Hoeveel ton woog de deksel die werd weggeblazen door de stoomexplosie?",
        "antwoorden": ["1000 ton", "1000ton", "duizend ton", "1000"],
        "hint": "Het is in tonnen uitgedrukt, niet in kilo’s."
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
    }
]

def vraag_stel(vraag, antwoorden, hint):
    fouten = 0
    typewriter("\n" + vraag)
    antwoorden = [a.lower() for a in antwoorden]

    while True:
        respons = veilige_input("Antwoord: ").strip().lower()

        if respons in antwoorden:
            clear_screen()
            typewriter("Correct! ✅")
            return
        else:
            fouten += 1
            typewriter("Fout antwoord.", color=RED)

            if fouten == 3:
                typewriter(f"Hint: {hint}")

# ===== MAIN =====
def main():
    for v in vragen:
        vraag_stel(v["vraag"], v["antwoorden"], v["hint"])

    clear_screen()
    typewriter("Alle vragen beantwoord!")
    typewriter("Voer het eindwachtwoord in:")

    while True:
        laatste = veilige_input("> ")
        if laatste == "9128":
            clear_screen()
            typewriter("Wachtwoord correct", 0.06)
            break
        else:
            typewriter("Onjuist wachtwoord.", color=RED)

main()
