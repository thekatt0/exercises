y = 1
while y == 1:
    num = input('Insert a number. ')
    answerList = []
    intNum = int(num)

    for x in range(1, intNum + 1):
        if intNum % x == 0:
            answerList.append(x)

    print(answerList)
    answer = input('Do you want to quit? ')
    if answer == 'yes':
            quit()


