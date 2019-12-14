from datetime import datetime

name = input('What is your name? ')
age = input('What is your age? ')
currentYear = datetime.now().year

x = 100 - int(age)


solution = currentYear + x


print(name + ', you will be 100 in ' + str(solution))