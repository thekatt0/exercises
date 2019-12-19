#inputs
numA = input('Insert the first number. ')
numB = input('Insert the second number. ')
numC = input('Insert the last number. ')

#convert to int
int(numA)
int(numB)
int(numC)

#comparisons not using max
if numA > numB and numA > n1umC:
        print(str(numA) + ' is the largest')

elif numB > numA and numB > numC:
        print(str(numB) + ' is the largest')

else:
    print(str(numC) + ' is the largest')
    