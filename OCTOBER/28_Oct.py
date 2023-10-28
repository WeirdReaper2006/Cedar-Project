# #PROCEDURE = VOID Function
# #FUNCTION = Fruitful functions
# def inputOddNumber():
#     number = 0
#     while number % 2 == 0:
#         number = int(input("Enter odd number: "))
#     return number
# #Main program starts here
# newNumber = inputOddNumber()
# print ("Number entered =",newNumber)

# ###########################################################

# def OutputSmbol(numberofsymbols, symbol):
#     for count in range(numberofsymbols):
#         print (symbol, end="")
#     print()
    
# #main program starts here
# OutputSmbol(10, "$")

# ###########################################################

# def sumRange( firstValue, lastValue):
#     sum = 0
#     for thisValue in range(firstValue, lastValue+1):
#         sum = sum + thisValue
#     return sum
# #main program starts here
# newNum = sumRange(1, 10)
# print (newNum)

#Task1: Make a funtion that takes 2 parameters and returns their sum
val1 = int(input("Enter first number: "))
val2 = int(input("Enter second number: "))
def addNumbers(Val1, Val2):
    sum = Val1+Val2
    return sum

Sum = addNumbers(val1, val2)
print (Sum)

#Task2: Make a function that calls another function that takes an input of a number and validates if its positive
#Output multiplacation table of the number in the first function
def func1():
    number = int(input("Enter even number: "))
    while number % 2 == 1:
        number = int(input("Enter even number: "))
    print ("Valid number entered")
    for i in range (1,11):
        print (f"{i}*{number} = {i * number}")
    

def func2():
    func1()

func2()