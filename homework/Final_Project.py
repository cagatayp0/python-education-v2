# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:57:13 2021

@author: cagat
"""


    
class Manager():
    def __init__(self, name, surname, age, language, salary, position, employees):
        self.name = name
        self.surname = surname
        self.age = age
        self.language = language
        self.salary = salary
        self.position = position
        self.employees = employees
        
    employeeList = []
            
            
                 
class Employee():
    def __init__(self, name, surname, language):
        self.name = name
        self.surname = surname      
        self.language = language
        
    languageList = dict()
             
    
    def AddLanguage(self):
        x = self.language
        self.languageList.update(x)
        
def PrintLanguage(Employee):
    a = Employee.languageList.keys()
    print(a)

a = Employee("Ali", "Duman", {"English" : 1, "Turkish" : 2})       
b = Employee("Ilkay", "Duduk", {"Japanese" : 1,"Turkish" : 2})
c = Employee("Hans", "Zimmer", {"German" : 1, "English" : 2})
d = Employee("Enzo", "Ferrari", {"Italian" : 1, "English" : 2})    

a.AddLanguage()
b.AddLanguage()
c.AddLanguage()
d.AddLanguage()

PrintLanguage(Employee)
