# Board = [[0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,0],]

# Board[1][5] = 6
# for row in range (6):
#     for col in range (7):
#         print (Board[row][col], end = "")
# print (Board)

#Task 1, 2, 3 and 4:
Sales = [[],
         [],
         [],
         [],
         []]
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum_all = 0

for row in range (0,5):
    for col in range (0,12):
        sale = int(input(f"Enter person {row + 1} sale {col + 1}: "))
        Sales[row].append(sale)
        sum_all = sum_all + sale
        if row == 0:
            sum1 = sum1 + Sales[0][col]
        if row == 1:
            sum2 = sum2+ Sales[1][col]
        if row == 2:
            sum3 = sum3 + Sales[2][col]
        if row == 3:
            sum4 = sum4 + Sales[3][col]
        if row == 4:
            sum5 = sum5 + Sales[4][col]
        
    
average1 = sum1 / 12
average2 = sum2 / 12
average3 = sum3 / 12
average4 = sum4 / 12
average5 = sum5 / 12
average_all = sum_all / 60
print (sum1, sum2, sum3, sum4, sum5,sum_all, average1, average2, average3, average4, average5, average_all)