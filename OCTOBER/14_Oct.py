from random import randint

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

print(randint(1,7))
#Task 3: use random for computer in rock paper scissors
while True:
    choice = int(input("Do you want to play Rock, Paper, Scissors? Press 1 for Yes and 2 for No: "))

    if choice != 1:
        print("Thank you for playing Rock, Paper, Scissors!")
        break

    user_choice = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    computer_choice = randint(1, 3)

    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a Draw")
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        print("You Win")
    else:
        print("Computer Wins")

print("Thank you for playing Rock, Paper, Scissors!")
