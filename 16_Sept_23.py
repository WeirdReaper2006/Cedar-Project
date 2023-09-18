#Case statements(there are no case statements so we used nested if statements)
Grade = input ("Enter your grade: ")

if Grade == "A":
    print ("Top Grade")
elif Grade =="F" or Grade =="U":
    print ("Fail")
elif Grade in ("B", "C", "D", "E"):
    print ("Pass")
else:
    print ("Invalid Grade")
    
#For Loops (count-controlled loop)
for x in range (5):
    print (x, end = " ")
    
print ()
for x in range (2, 14, 3):
    print (x, end = " ")
    
print ()
for x in range (5, 1, -1):
    print (x, end = " ")
    
print ()
for x in ("a", "b", "c"):
    print (x, end = " ")
    
print ()


#Q1) Ask a user for a number and print its multiplication table (1-10)
num = int(input("Enter a Number : "))
for x in range (1, 11):
    ans = num * x
    print (f"{x} * {num} = {ans}")
    
#Q2) Use for loop to output all odd numbers between 1000 and 10000
for x in range(1001, 10000, 2):
    print (x)

#Q3) Ask user for size of triangle and print a right angled triangle of that height
num = int(input("Enter a Number: "))
for x in range(1, num+1):
    print ("* " * x)

#Q4) Ask user for size of pyramid and output a pyramid of that height
num = int(input("Enter the height of the pyramid: "))

for line in range(1, num + 1):
    # Print spaces for each row
    for spaces in range(num - line):
        print(" ", end="")
    
    # Print '#' characters for each row
    for hashes in range(line * 2 - 1):
        print("# ", end="")
    
    # Move to the next line for the next row
    print()

#Q5) Ask user for the number of fishes and size of the fsh and print that many fishes