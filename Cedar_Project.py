# print ("hello, World")

# var = 10
# print (var)
# var = var + 10
# print(var+5)
# print(var-5)
# print(var/5)
# print(var*5)
# print(var**5)
# print(var//5)
# print(var%5)

# print ("My number is",var)
# #Alternate method is:
# #print (f"My number is {var}")

# name = input("Enter your name: ")
# print (f"Hello {name}")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print (num1 + num2)

# #Formatting numbers
# print ("My number is {0}. Your number is {1}.".format(num1,num2))
# #Alt method:
# print (f"My number is {num1}. Your number is {num2}.")

# x = int(input("Enter a number: "))
# if x < 0:
#     print ("Negative")
# else:
#     print ("Positive")
    
#Q1) Ask user for their age and output if the user is an adult or not
age = int(input("Enter age: "))
if age >= 18:
    print ("You're an Adult")
else:
    print ("You're not an Adult")
    
#Q2) Ask the user if monkey A and monkey B are smiling. If either or oth are smiling, you are in trouble
monkeyA_smiling = bool(input("Is monkey A smiling? "))
monkeyB_smiling = bool(input("Is monkey B smiling? "))
if monkeyA_smiling or monkeyB_smiling:
    print ("You're in trouble.")
else:
    print ("You're not in trouble.")
    
#Q3) Ask user if he/she is on vacation and if it is a weekday. output if the user can sleep in late
vacation = bool(input("Are you on vacation?"))
weekday = bool(input("is it a weekday?"))
if vacation or weekday:
    print("Sojao")
else:
    print("You are safe")
    
#Q4) Ask user for their lucky number and output if the lucky number is odd or even
lucky_num = int(input("What's your lucky number: "))
if lucky_num % 2 == 0:
    print("Even")
else:
    print("Odd")