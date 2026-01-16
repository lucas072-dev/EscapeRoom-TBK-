import time
import sys

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def progress_bar():
    stappen = 50

    bar_lengte = 30

    print("Laden: ", end='', flush=True)

    for i in range(stappen + 1):

        percent = (i / stappen) * 100

        blokjes = i * bar_lengte // stappen

        bar = '█' * blokjes + '░' * (bar_lengte - blokjes)

        print(f'\r[{bar}] {percent:.1f}%', end='', flush=True)

        time.sleep(0.1)

    print("\n Gevalideerd!")

# ===== START WACHTWOORD =====
typewriter("Voer het wachtwoord in:", 0.07)
wachtwoord = input("> ")

if wachtwoord == "1908":
    typewriter("✅ Het wachtwoord is correct!\n")
else:
    typewriter("❌ Het wachtwoord is incorrect!")
    sys.exit()

progress_bar()

# ===== VRAGEN =====
vragen = [
    {
        "vraag": "Vraag 1: Hoeveel meer radioactieve straling was er bij de superwolven dan wat volgens de menselijke veiligheidslimiet mag?",
        "antwoord": "6 keer",
        "hint": "Het is een enkel cijfer, en best een klein getal."
    },
    {
        "vraag": "Vraag 2: Hoeveel ton woog de deksel die werd weggeblazen door de stoomexplosie?",
        "antwoord": "1000 ton",
        "hint": "Het is in tonnen uitgedrukt, niet in kilo’s."
    },
    {
        "vraag": "Vraag 3: Welke naburige stad werd ook getroffen door de explosie van Tsjernobyl?",
        "antwoord": "pripjat",
        "hint": "De stad ligt op korte afstand van de kerncentrale."
    },
    {
        "vraag": "Vraag 4: Hoe groot was de vervreemdingszone rond de kerncentrale?",
        "antwoord": "30 km",
        "hint": "Het aantal is kleiner dan 50, een mooi rond getal."
    }
]

def vraag_stel(vraag, antwoord, hint):
    typewriter("\n" + vraag)
    respons = input("Jouw antwoord: ")

    if respons.lower().strip() == antwoord.lower():
        typewriter("Correct! ✅")
        return True
    else:
        typewriter(f"❌ Fout! Het juiste antwoord was: {antwoord}")
        typewriter(f"💡 Hint: {hint}")
        return False

def main():
    for v in vragen:
        if not vraag_stel(v["vraag"], v["antwoord"], v["hint"]):
            typewriter("\nJe bent afgevallen. Probeer het opnieuw.")
            return

    typewriter("\n🎯 Alle vragen goed beantwoord!")
    typewriter("Voer het eindwachtwoord in:")

    laatste = input("> ")
    if laatste == "9128":
        typewriter("🎉 Eindwachtwoord correct! Je hebt het gehaald!", 0.06)
    else:
        typewriter("❌ Fout eindwachtwoord. Probeer later opnieuw.")

main()
