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
rounds = int(input("Enter number of rounds: "))
p1Score = 0
p2Score = 0
for i in range (rounds):
    p1Input = input("Player 1, Enter r, s or p: ")
    while p1Input != "r" and p1Input != "s" and p1Input != "p":
        print ()
        
#Q4, ask user to think of a number between 1 and 100
#your program can ask yes or no questions (max 10)
#your program should tell the correct guess everytime
print ("Please think of a number between 1 and 100: ")
Q1 = input("Is your number even. Enter y or n: ")

