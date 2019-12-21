#word input
str = input('Give me a word. ')

#palindrome check with index reverse
if str.lower() == str[::-1].lower():
    print(str + ' is a palindrome.')
else:
    print(str + ' is not a palindrome.')
