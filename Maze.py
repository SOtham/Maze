from doctest import master
import tkinter as tk
from tkinter import ttk
from gridSetup import *

#class to create maze window which will display a grid of cells
class Maze(tk.Tk):
    #constructor
    def __init__(self, rows, columns):
        super().__init__()
        self.master = master
        self.title("Maze")

        #creating maze object
        maze = CellGrid(self,rows,columns,(((self.winfo_width()+self.winfo_height())/2)/columns)*750)
        maze.pack()