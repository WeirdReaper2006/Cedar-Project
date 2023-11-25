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
        
print (FindSumFrom1 (15))