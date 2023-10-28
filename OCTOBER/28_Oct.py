#PROCEDURE = VOID Function
#FUNCTION = Fruitful functions
def inputOddNumber():
    number = 0
    while number % 2 == 0:
        number = int(input("Enter odd number: "))
    return number
#Main program starts here
newNumber = inputOddNumber()
print ("Number entered =",newNumber)

###########################################################

def OutputSmbol(numberofsymbols, symbol):
    for count in range(numberofsymbols):
        print (symbol, end="")
    print()
    
#main program starts here
OutputSmbol(10, "$")

###########################################################

def sumRange( firstValue, lastValue):
    sum = 0
    for thisValue in range(firstValue, lastValue+1):
        sum = sum + thisValue
    return sum
#main program starts here
newNum = sumRange(1, 10)
print (newNum)