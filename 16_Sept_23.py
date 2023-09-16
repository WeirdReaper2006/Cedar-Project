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