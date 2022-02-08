#import
from  tkinter import *    
import puzzle_generator
from tkinter import messagebox

import random
sudoku=[]
choices=[x for x in range(0,9)]
sudoku=puzzle_generator.helper()
for i in range(9):
    rand_no=random.randrange(4,7)
    while(rand_no>0):
    	 j=random.choice(choices)
    	 if(sudoku[i][j]!=0):
    	 	sudoku[i][j]=0
    	 	choices.remove(j)
    	 	rand_no-=1
    choices=[x for x in range(0,9)]

    	 



#initialisation
root=Tk()
root.resizable(False,False)
root.title("Sudoku")
root.geometry("600x700")
#root.iconbitmap('/home/divyanshubist/Desktop/sudoku-solver/icon.ico')


#frame changing function
def start_puzzle_func():
    
    start_frame.forget()
    Sudoku_frame.pack(fill='both',expand=1) 
    return 

def game_finish_func():
    return

#frames
start_frame=LabelFrame(root)
Sudoku_frame=LabelFrame(root)


#start_frame
name_label=Label(start_frame,text="Sudo-ku",font=('Arial',70),padx=140,pady=100)
name_label.place(x=0,y=50)
start_game_btn=Button(start_frame,text="New Game",padx=50,pady=20,command=start_puzzle_func,bg="#5b155e",fg="#41f713",borderwidth=2,relief="raised",font=('Arial',20))
start_game_btn.place(x=180,y=350)


#Sudoku_frame

def only_numbers(char,allowed):
    if(allowed==''):
         return True
    return char.isdigit() and (int(allowed)>=1 and int(allowed)<=9)
label=Label(Sudoku_frame,text="",borderwidth=5,relief="solid",padx=0,pady=0,bg="#000000")
label.place(x=93,y=93,width=390,height=390)

x_val=100
y_val=100
for i in range(9):
         if(i==3 or i==6):
             y_val=y_val+7
         for j in range(9):
               if(j==3 or j==6):
                     x_val=x_val+7
               if(sudoku[i][j]!=0):
                     new_label=Label(Sudoku_frame,text=sudoku[i][j],padx=8,pady=8,font=('Arial',13),borderwidth=0.5,relief="solid")
                     new_label.place(x=x_val,y=y_val,width=40,height=40)
               else:
                     validation=Sudoku_frame.register(only_numbers)
                     new_entry=Entry(Sudoku_frame,font=('Arial',16),borderwidth=1,relief="solid",validate="key",validatecommand=(validation,'%S','%P'))
                     new_entry.place(x=x_val,y=y_val,width=39,height=39)
                     new_entry.insert(1," ")
               x_val=x_val+40
         y_val=y_val+40
         x_val=100
                




#start of program 

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?\nChanges will not be saved and you have to start again"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
start_frame.pack(fill="both",expand=1)
root.mainloop()
