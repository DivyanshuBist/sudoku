import random 
row=9
col=9
sudoku=[]
row_nos=[]
col_nos=[]
block_nos=[]

for i in range(row):
    row_nos.append(0)
    col_nos.append(0)
    block_nos.append(0)

def no_generator(i,j):
    block_row=int(i/3)*3
    block_col=int(j/3)*3
    k=block_row+int(block_col/3)
    while(True):
	    rand_no=random.randrange(0,9)
	    if((row_nos[i]&(1<<rand_no))==0 and (col_nos[j]&(1<<rand_no))==0 and (block_nos[k]&(1<<rand_no))==0):
                row_nos[i]=row_nos[i]|(1<<rand_no)   
                col_nos[j]=col_nos[j]|(1<<rand_no)
                block_nos[k]=block_nos[k]|(1<<rand_no)
 #               print(i,row_nos[i],j,col_nos[j],k,block_nos[k])
                break
    return rand_no


for i in range(row):
    cols=[]
    rand_no=random.randrange(2,7)
    for j in range(col):
        put=random.randrange(2)
        if(put==1 and rand_no>0):
                no=no_generator(i,j);
                cols.append(no)
                #print("generated",i,j,no,"\n")
                rand_no=rand_no-1
        else:
#            print(i,j,0,"\n")
            cols.append(0)
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
