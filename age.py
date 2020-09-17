# age problem thing

import datetime
now = datetime.datetime.now()
name = input("Input your first name: ")
age = int(input("Input your current age: "))
year = int(input("Input a year: "))

yearBorn = now.year - age
while year <= yearBorn:
    print(f'{name}, please enter a year after the year you were born: {yearBorn}')
    year = int(input("Input a year: "))
    
print(f'By the end of {year}, you should be {year - yearBorn} years old!')
