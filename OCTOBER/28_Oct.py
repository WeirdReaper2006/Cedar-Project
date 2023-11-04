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
    for i in range(numberofsymbols):
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

#ARRAYS : python cant have arrays so we use lists
list1 = []
list1.append("wasim akram")
list1.append("virat kohli")
list1.append("viv richards")
print("value at index 2 =", list1[2])
print("Lenght of list =", len(list1))
list1[2] = "shahid afridi"
for i in range(len(list1)):
    print(list1[i])

list2 = [0,0,0,0,0]
print("values in list2")
for i in range(len(list2)):
    print(list2[i])

#arrayname = [initVal for i in range(size)]
list3 = [0 for i in range(100)]
print("list 3 values")
for i in range(len(list3)):
    print("index",i,"=",list3[i])
    
#Task 1:
names = []
for i in range(10):
    name1 = input("Enter a name: ")
    names.append(name1)
    
print (names)

#Task 2:
output = "Output not found"
name2 = input("Enter a name: ")
for i in range(len(names)):
    if name2 == names[i]:
        output = f"Index is {i}"

print (output)

#Task 3, 4, 5 and 6:
#(Assuming that the total marks for the quiz is 10)

cs_marks = []
highest = 0
lowest = 10
sum = 0
std_names = []
highest_index = 0
lowest_index = 0
    
for i in range (10):
    name = input (f"Enter {i + 1} student's name: ")
    std_names.append(name)
    
    mark = int(input(f"Enter {i + 1} student's marks: "))
    while mark < 0 and mark > 10:
        mark = int(input(f"Enter {i + 1} student's marks: "))
    cs_marks.append(mark)
    sum = sum + mark
    if mark > highest:
        highest = mark
        highest_index = i
        highest_student = std_names[i]
    if mark < lowest:
        lowest = mark
        lowest_index = i
        lowest_student = std_names[i]
        
average = sum /10
print(f"The student with the highest marks is {highest_student}. The student with the lowest marks is {lowest_student}")

#Task 7:

n = len(cs_marks)
for i in range(n - 1):
    swap = False
    for j in range(0, n - i - 1):
        if cs_marks[j] < cs_marks[j + 1]:  # Change the comparison to sort in descending order
            cs_marks[j], cs_marks[j + 1] = cs_marks[j + 1], cs_marks[j]
            std_names[j], std_names[j + 1] = std_names[j + 1], std_names[j]
            swap = True
    if not swap:
        break

print("Students sorted by marks in descending order:")
for i in range(10):
    print(f"{std_names[i]}: {cs_marks[i]}")