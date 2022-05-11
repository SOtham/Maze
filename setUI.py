import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import Maze as maze

#class to get user to input number of rows and columns for cell grid
class setUI(tk.Tk):
    #constructor
    def __init__(self):
        super().__init__()
        self.title("Maze Solver")
        self.geometry("300x300")
        self.resizable(False, False)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.setLayout()

    #setting layout of window
    def setLayout(self):
        rowLabel = ttk.Label(self,text="Number of Rows")
        rowLabel.grid(row=0,column=0,padx=5,pady=10, sticky=tk.W)

        self.rowInput = ttk.Entry(self)
        self.rowInput.grid(row=0,column=1, pady=10)

        columnLabel = ttk.Label(self,text="Number of Columns")
        columnLabel.grid(row =1,column=0, padx=5, sticky=tk.W)

        self.columnInput = ttk.Entry(self)
        self.columnInput.grid(row=1,column=1)

        btnInput = ttk.Button(self,text="Generate",command= lambda: self.createMaze())
        btnInput.grid(row=2,column=1, sticky=tk.NW, padx=23, pady =10)
        
    #creating maze window
    def createMaze(self):
        if((int(self.rowInput.get()) < 101 and int(self.columnInput.get()) < 101) and (int(self.rowInput.get()) > 0 and int(self.columnInput.get()) > 0)):
            mazeWindow = maze.Maze(int(self.rowInput.get()), int(self.columnInput.get()))
            mazeWindow.mainloop()
        else:
            msg.showwarning(title = "error" , message = "Please enter a number between 1 and 100")
        