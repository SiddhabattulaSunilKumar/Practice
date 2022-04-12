import random

# WHo will pay the bill

People_Names=[]
Number_Of_Persons = input("Enter the all Names with comman : ")
People_Names= Number_Of_Persons.split(",")
People_Name_Choice = random.choice(People_Names)