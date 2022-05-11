import tkinter as tk
from tkinter import ttk
import Maze as maze


class setUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maze Solver")
        self.geometry("300x300")
        self.resizable(False, False)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.setLayout()


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
    
    def createMaze(self):
        mazeWindow = maze.Maze(int(self.rowInput.get()), int(self.columnInput.get()))
        mazeWindow.mainloop()
