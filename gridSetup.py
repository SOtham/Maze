from itertools import count
from math import ceil
from tkinter import *


class Cell():
    #defining colours for diffrent cell states
    fillerColour= "black"
    borderColour= "black"
    emptyColour= "white"
    startColour = "green"
    endColour = "red"
    #constructor
    def __init__(self, master, x, y, size):
        self.master = master
        self.x = x
        self.y = y
        self.size = size
        self.fill = False
        self.start = False
        self.end = False
    #funcition to change fill of a cell
    def switch(self):
        self.fill = not self.fill
    #function to draw cell
    def draw(self):
        if self.master != None:
            fill = Cell.fillerColour
            outline = Cell.borderColour

            if not self.fill:
                fill = Cell.emptyColour
                outline = Cell.borderColour
            
            if self.start:
                fill = Cell.startColour
                outline = Cell.borderColour
            if self.end:
                fill = Cell.endColour
                outline = Cell.borderColour

            xMin = self.x * self.size
            yMin = self.y * self.size
            xMax = xMin + self.size
            yMax = yMin + self.size

            self.master.create_rectangle(xMin, yMin, xMax, yMax, fill = fill, outline = outline)
#class to create canvas to draw cells on
class CellGrid(Canvas):
    #constructors
    def __init__(self, master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width= cellSize*columnNumber, height = cellSize*rowNumber, *args, **kwargs)
        self.cellSize = cellSize
        #counters to count number of start and end cells
        self.countStart = 0
        self.countEnd = 0
        #list to store all cells
        self.gridList=[]
        for row in range(rowNumber):
            line =[]
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize))

            self.gridList.append(line)
        #drawing grid of cells
        self.draw()
        #list to track cells that are switched
        self.switched=[]
        #binding mouse buttons
        self.bind("<Button-1>", self.hadelMouseClick)
        self.bind("<B1-Motion>", self.handleMouseMotion)
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        self.bind("<Button-3>", self.handelStart)

        self.bind("<Button-2>", self.handelEnd)
    #fuction to draw grid
    def draw(self):
        for row in self.gridList:
            for cell in row:
                cell.draw()
    #function to return row and column of cell that was clicked
    def eventCells(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column
    #function to handle mouse click
    def hadelMouseClick(self, event):
        row, column = self.eventCells(event)
        cell = self.gridList[row][column]
        if cell.start == False and cell.end == False:
            cell.switch()
            cell.draw()
            self.switched.append(cell)
    #function to handle mouse motion
    def handleMouseMotion(self, event):
        row,column = self.eventCells(event)
        cell = self.gridList[row][column]
        if cell not in self.switched and cell.start == False and cell.end == False:
            cell.switch()
            cell.draw()
            self.switched.append(cell)
    #function to handel start cell
    def handelStart(self, event):
        row, column = self.eventCells(event)
        cell = self.gridList[row][column]
        if cell.fill == False and cell.end == False and cell.start == False:
            if(self.countStart <1):
                cell.start = True
                self.countStart += 1
                cell.draw()
        elif cell.start == True:
            cell.start = False
            self.countStart -= 1
            cell.draw()
        print(self.countStart)
    #function to handel end cell
    def handelEnd(self, event):
        row, column = self.eventCells(event)
        cell = self.gridList[row][column]
        if cell.fill == False and cell.start == False and cell.end == False:
            if(self.countEnd <1):
                cell.end = True
                self.countEnd += 1
                print(self.countEnd)
                cell.draw()
        elif cell.end == True:
            cell.end = False
            self.countEnd -= 1
            cell.draw()
