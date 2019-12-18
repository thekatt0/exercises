#initializing lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

#list comparison function
def listCompare(list1, list2, newList):
    for numA in list1:
        for numB in list2:
            if numA == numB:
                numC = numA
                newList.append(numC)

#function call
listCompare(a, b, c)

#duplicates removal
c = list(dict.fromkeys(c))

#printing result
print(c)                  