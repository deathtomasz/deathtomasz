
firstnum = 0
secNum = 0
reset = True
rezultat  = 0
operacjaLista = ["+", '-','*','/','**']
operacja = None

while True:
    if reset == True:
        try:
            firstNum = int(input("Nowe obliczenie! \n Wprowadź pierwszą liczbę : \n"))
            reset = False
            print(reset)
        except:
            print("To nie jest liczba!")
            continue
        operacja = input("Wprowadz rodzaj operacji z listy: \n" + str(operacjaLista) + '\n' + "możesz też wpisać ""exit"" lub ""reset"". \n")  

        if operacja == "reset":
            reset = True
            continue
        if operacja == "exit": break
        if operacja not in operacjaLista:
            print("Operacji nie ma na liście \n \n")
            reset = True
            continue


        while reset == False:

            secNum = input("Wprowadź DRUGĄ liczbę : \n")
            if secNum == str("exit"):
                break
            if secNum == str("reset"): 
                reset = True
                        
                print("To nie jest liczba!")            
                continue         
            
            if operacja == "+":
                rezultat = firstNum + int(secNum)
            if operacja == "-":
                rezultat = firstNum - int(secNum)              
            if operacja == "*":
                rezultat = firstNum * int(secNum)              
            if operacja == "/":
                rezultat = firstNum / int(secNum)              
            if operacja == "**":
                rezultat = firstNum ** int(secNum)

            print('\n Wynik operacji '+ str(firstNum) + operacja + str(secNum) + " = " + str(rezultat)+'\n\n')
            rezultat = None
            reset = True
    continue
        