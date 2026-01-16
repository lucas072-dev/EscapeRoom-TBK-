import time
import sys

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ===== START WACHTWOORD (ONBEPERKT) =====
while True:
    typewriter("Voer het wachtwoord in:", 0.07)
    wachtwoord = input("> ")

    if wachtwoord == "1908":
        typewriter("✅ Het wachtwoord is correct!\n")
        break
    else:
        typewriter("❌ Onjuist wachtwoord.\n")

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
    fouten = 0
    typewriter("\n" + vraag)

    while True:
        respons = input("Jouw antwoord: ").strip().lower()

        if respons == antwoord.lower():
            typewriter("Correct! ✅")
            return  # pas NU naar de volgende vraag
        else:
            fouten += 1
            typewriter("❌ Fout antwoord.")

            if fouten == 3:
                typewriter(f"💡 Hint: {hint}")

def main():
    typewriter("De quiz begint...\n", 0.06)

    for v in vragen:
        vraag_stel(v["vraag"], v["antwoord"], v["hint"])

    typewriter("\n🎯 Alle vragen beantwoord!")
    typewriter("Voer het eindwachtwoord in:")

    while True:
        laatste = input("> ")
        if laatste == "9128":
            typewriter("🎉 Eindwachtwoord correct! Je hebt het gehaald!", 0.06)
            break
        else:
            typewriter("❌ Fout eindwachtwoord. Probeer opnieuw.")

main()
