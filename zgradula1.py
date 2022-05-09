from ast import Try
from random import random


imie = str(input('Weno podaj imię, najlepiej swoje.\n'))

if imie:
    print(f'Fajnie! Umiesz pisać {imie}. To się przyda!\n')
else:
    print("Nie wpisałeś imienia, ta gra będzie dla ciebie za trudna!. Idź stąd!! Już!")
    exit

shootcount = 1
import random
szukana = random.randint(0, 100)
szczalgracza = int
goodShot = False

while not goodShot:

    try:
    
        szczalgracza = int(input('Szczelaj!\n'))

        if szczalgracza in range(0,100):

            if szczalgracza > szukana:
                print(f'nie, bo mniejsza')
                

                shootcount += 1
                
            elif szczalgracza < szukana:
                print(f'a wcale nie - wieksza')
                shootcount += 1
                
            elif szczalgracza == szukana:
                print(f'Brawo\n strzeliłeś {shootcount} razy. Zajmij się lepiej czymś poważniejszym!\n')    
                goodShot = True
        else:
            print("Podaj cyfrę z zakresu 0 - 100!\n")
    except:
        print("Nie podałeś cyfry, tylko jakieś znaczki...")

print("Nara!")