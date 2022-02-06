#import
from  tkinter import *    
import solver
from tkinter import messagebox
from PIL import Image, ImageTk

#initialisation
root=Tk()
root.resizable(False,False)
root.title("Sudoku")
root.geometry("600x700")
#root.iconbitmap(/home/divyanshubist/Desktop/sudoku-solver/icon.png)


#frame changing function
def start_puzzle_func():
    Sudoku_frame.pack(fill='both',expand=1)
    start_frame.forget()
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



#window close function
def close():
    root.destroy()

#Sudoku_frame
timer_label=Label(Sudoku_frame,text="Timer",pady=30,padx=10,font=('Arial',15))
timer_label.place(x=280,y=550)
btn=Button(Sudoku_frame,text="close",command=close)
btn.pack()

#start of program 

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?\nChanges will not be saved and you have to start again"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
start_frame.pack(fill="both",expand=1)
root.mainloop()
