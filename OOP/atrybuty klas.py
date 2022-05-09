
from types import NoneType
from unicodedata import name

class klasaStudent:
    def __init__(self, name, surname, age , city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolname = None
        self.kierunki = None

    def studentInfo(self):
        print(self.name,
            self.surname, 
            self.age,
            self.city,
            self.schoolname,
            self.kierunki)

import random
class klasaSchool:
    def __init__(self, schoolname, city):
        self.schoolname =schoolname
        self.city = city
        self.studentlist = []
        self.kierunki= ['matma', 'biola', 'polak']

    def addStudent(self, student):
        if isinstance(student, klasaStudent):
            self.studentlist.append(student)
            student.schoolname = self.schoolname  #ttauj jest równizca względem filmu
            student.kierunki = random.choice(self.kierunki)

    def schoolINFO(self):
        print('Nazwa szkoły: ',self.schoolname, self.city)
        print('Studenci: ')
        for el in self. studentlist:
            el.studentInfo()
import os 
clear = lambda: os.system("cls")

student1 = klasaStudent('marek','chujel', 14,'uć')
student1.schoolname = 'podstawowka3'
student1.country = 'spain'
student1.studentInfo()
print(student1.country)
student2 = klasaStudent('tomek','pluci', 66,'pece')

szkoła1 = klasaSchool('polibuda', 'Uć')
szkoła1.addStudent(student1)
szkoła1.addStudent(student2)
szkoła1.schoolINFO()
