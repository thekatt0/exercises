num = input('Enter a number. ')
check = input('Enter a number to divide it by. ')

if (int(num) % int(check)) == 0:
    print(str(num) + ' is divisible by ' + str(check))

else:
    print(str(num) + ' is not divisible by ' + str(check))
