def recursiveFunction (num1):
    print (num1)
    if num1 < 5:
        recursiveFunction (num1+1)
    
#Task1: Make a recursive function that counts down from the parameter given till 1
def countDown (num2):
    print (num2)
    if num2 > 1:
        countDown (num2 - 1)
        
#Task2: Make a function that returns the sum of all value from parameter number
def FindSumFrom1 (num3):
    if num3 > 1:
        return num3 + FindSumFrom1 (num3 - 1)
    else:
        return 1
        
#Task3: Make a recursive funtion that takes a position number value as input and output fibonacci sequence till that position
def Fibonacci (position):
    if position == 1:
        return [1]
    elif position == 2:
        return [1,1]
    else:
        fib_sequence = Fibonacci (position - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
    
print (Fibonacci(8))