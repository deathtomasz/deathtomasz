import os
import random
clear = lambda: os.system("cls")
class Student:
    def __init__(self, name, surnmane, age, city):
        self.name = name
        self.surnmane = surnmane
        self.age = age
        self.city = city
        self.shoolname = None
        self.kierunek = None
        
    def printInfo(self):
        print(        
            self.name,
            self.surnmane,
            self.age,
            self.city,
            self.shoolname,
            self.kierunek)
class Szkoła:
    def __init__(self, szname, szcity):
        self.name = szname
        self.szname = szname
        self.szcity = szcity 
        self.kierunki = ["biola", "matma", "polak","gegra", "fiza"]
        self.studentList = []

    def addStudent(self, student):
        if isinstance(student, Student):
            self.studentList.append(student)
            student.shoolname = self.name
            student.kierunek = random.choice(self.kierunki)

    def printShoolinfo(self):
        print("szkoła to:", self.szname, " w mieście :", self.szcity)
        print("uczniowie :")
        for el in self.studentList:
            el.printInfo()
            
student1 = Student("kasia", "pipa", 45, "karowk")
student1.shoolname = "I LO"
# student1.printInfo()
student2 = Student("miachas","jeaniutki",66,"pacanow")
szkola = Szkoła("polibuda", "uc")
szkola.addStudent(student1)
szkola.addStudent(student2)
szkola.printShoolinfo()



