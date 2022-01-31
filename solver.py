from random import random 
import math 
row=9
col=9

sudoku=[]
for i in range(row):
    cols=[]
    rand_no=math.ceil(random()*1000000007)
    for j in range(col):
        cols.append(math.floor((random()*rand_no)%10))
    sudoku.append(cols)


        

for r in sudoku: 
    print(r)
def solver(sudoku,row,col):
    if(row==9):
        for r in sudoku:
            print(r,end=" ")
        print()
    new_row=row
    new_col=col+1
    if(col==8):
        new_row=row+1
        new_col=0
    for val  in range(1,9,1):
        if(possible):
            sudoku[row][col]=val
            solver(sudoku,new_row,new_col)
            sudoku[row][col]=0
