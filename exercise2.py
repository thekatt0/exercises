num = input('Enter a number. ')

if (int(num) % 4) == 0:
    print(str(num) + ' is divisible by 4.')

elif (int(num) % 2) == 0:
    print(str(num) + ' is an even number.')

else:
    print(str(num) + ' is an odd number.')
