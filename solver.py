import random 
row=9
col=9

#for i in range(0,row):
#    cols=[]
#    for j in range(0,col):
#        cols.append(0)
#    sudoku.append(cols)



def check(sudoku,row,col,val):
    for i in range(0,9):
    	if(sudoku[i][col]==val):
           return False
    for i in range(0,9):
        if(sudoku[row][i]==val):
           return False
    block_row=int(row/3)*3
    block_col=int(col/3)*3
    for i in range(block_row,block_row+3,1):
        for j in range(block_col,block_col+3,1):
           if(sudoku[i][j]==val):
            	return False               
    return True   
    


def generator(sudoku,row,col,lst):
    if(row==9):
        global done
        done=True
        return 
    new_row=row
    new_col=col+1
    length=len(lst)
    remain=[]
    while(length>0):
    	val=random.choice(lst)
    	if(check(row,col,val)==True):
    		sudoku[row][col]=val
    		lst.remove(val)
    		new_list=lst.copy()
    		new_list.extend(remain)
    		if(col==8):
    			new_list=[x for x in range(1,10)]
    			new_row=row+1
    			new_col=0
    		generator(sudoku,new_row,new_col,new_list)
    		if(done==True):
    			return
    		else:    			 
    			sudoku[row][col]=0
	    		remain.append(val)
    	else:
    		lst.remove(val)
    		remain.append(val)
    	length=length-1

done=False 

lst=[x for x in range(1,10)]          	

def helper(sudoku):
    for i in range(row):
        rand_no=random.randrange(2,7)
        for j in range(col):
                pos=random.randrange(0,2)
                if(pos==0 and rand_no>0):
                      sudoku[i][j]=0


            
