from datetime import datetime

name = input('What is your name? ')
age = input('What is your age? ')
linesNumber = input('Enter another number. ')
currentYear = datetime.now().year

x = 100 - int(age)


solution = currentYear + x

for i in range(int(linesNumber)):
    print(name + ', you will be 100 in ' + str(solution) + '\n')