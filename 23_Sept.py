# Q1. convert the triangle code to only use while loop
num = int(input("Enter a Number: "))
i = 0
while i <= num:
    print ("* " * i)
    i +=1
    
# Q2. convert the pyramid code to only use while loop 
num = int(input("Enter the height of the pyramid: "))
line = 0
while line in range(0, num + 1):
    # Print spaces for each row
    spaces = 0
    while spaces in range(num - line):
        print(" ", end="")
        spaces +=1
    
    # Print '#' characters for each row
    hashes = 0
    while hashes in range(line * 2 - 1):
        print("#", end="")
        hashes +=1
    
    # Move to the next line for the next row
    print()
    line +=1
# Q3. create a two player rock , paper , scissor , game which vaidates the user innput
# ask user for the number of rounds, output winner of each round and overall game
