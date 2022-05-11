from doctest import master
import tkinter as tk
from tkinter import ttk
from gridSetup import *

class Maze(tk.Tk):
    def __init__(self, rows, columns):
        super().__init__()
        self.master = master
        self.title("Maze")
        
        maze = CellGrid(self,rows,columns,10)
        maze.pack(pady = 10)