print ("hello, World")

var = 10
print (var)
var = var + 10
print(var+5)
print(var-5)
print(var/5)
print(var*5)
print(var**5)
print(var//5)
print(var%5)

print ("My number is",var)
#Alternate method is:
#print (f"My number is {var}")

name = input("Enter your name: ")
print (f"Hello {name}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print (num1 + num2)

#Formatting numbers
print ("My number is {0}. Your number is {1}.".format(num1,num2))
#Alt method:
print (f"My number is {num1}. Your number is {num2}.")

x = int(input("Enter a number: "))
if x < 0:
    print ("Negative")
else:
    print ("Positive")
    
#Q1) Ask user for their age and output if the user is an adult or not
age = int(input("Enter age: "))
if age >= 18:
    print ("You're an Adult")
else:
    print ("You're not an Adult")