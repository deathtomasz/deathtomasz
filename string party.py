
import string
import os

haslo = "Gdyby ten to ten"
charGiven = input("Podaj literę \n")


def zamiana():
    clear = lambda: os.system("cls")
    clear()
    haslo_odkrywane = haslo # ta wiem, po ang ma być :D
    cuttedToDeath = []
    for a in haslo_odkrywane:
        cuttedToDeath.append(a)
    print(cuttedToDeath)


zamiana()

