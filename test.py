import time
import sys

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

typewriter("password:", 0.07)
input()
if input == "1908":
	typewriter("De password is correct!")
else:
	typewriter("De password is incorrect!")

 
