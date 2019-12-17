num = input('Insert a number. ')
answerList = []
intNum = int(num)

for x in range(1, intNum + 1):
    if intNum % x == 0:
        answerList.append(x)

print(answerList)

