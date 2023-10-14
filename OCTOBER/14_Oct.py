from pickle import FALSE
from tkinter import TRUE


myStr = "This is Cedar College"
print(myStr[5])
print(chr(65))
print(ord("a"))
print(len(myStr))
#start:end]
#left empty: start = 0
#right empty: end = length
#left nog: start - longth - value
#right nog: end = length - value
#MID
print(myStr[2:6])
print(myStr[0:5])
#LEFT
print(myStr[:5])
print(myStr[:-7])
#RIGHT
print(myStr[14:])
print(myStr[-7:])

print(myStr.upper())
print(myStr.lower())
myNum = 7.99
print(int(myNum))
strNum = "7"
print(int(strNum))
strNum2 = "7.45"
print(float(strNum2))

#Task 1: Ask user for a string and output if string is a palindrome
string = input("Enter a word: ")
is_palindrome = True
for x in range(len(string) // 2):
    if string[x] != string[-x - 1]:
        is_palindrome = False
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
#Task 2: Ask user for a string, convert and store it in reverse
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)