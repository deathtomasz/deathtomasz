clear = lambda: os.system("cls")
class pies:
    def __init__(self, rasa, dogname="fafik"):
        self.rasaChesk(rasa)
        self.dogname = dogname

    def  rasaChesk(self, rasa):
        if rasa != "spaniel" and rasa != "cocker":
            self.rasa = rasa
            print(rasa)
        else:
            print("Zła rasa, fuj!") 

    def printD(self):
        print(self.rasa, self.dogname)

pies1 = pies("koles")
pies1.age = 666
pies1.printD()
print(pies1.age)