#random module
import random

#initializing lists
a = []
b = []
c = []

#random numbers generation
for num in range(20):
    a.append(random.randint(1,20))

for num in range(20):
    b.append(random.randint(1,20))

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