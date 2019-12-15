list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
listSmall = []


for num in list:
    if num < 5:
        listSmall.append(num)

for smallNum in listSmall:
    print(smallNum)
