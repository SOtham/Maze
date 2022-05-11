from tkinter import *


class Cell():
    fillerColour= "black"
    borderColour= "black"
    emptyColour= "white"
    start_colour = "green"
    end_colour = "red"

    def __init__(self, master, x, y, size):
        self.master = master
        self.x = x
        self.y = y
        self.size = size
        self.fill = False

    def switch(self):
        self.fill = not self.fill

    def draw(self):
        if self.master != None:
            fill = Cell.fillerColour
            outline = Cell.borderColour

            if not self.fill:
                fill = Cell.emptyColour
                outline = Cell.borderColour

            xMin = self.x * self.size
            yMin = self.y * self.size
            xMax = xMin + self.size
            yMax = yMin + self.size

            self.master.create_rectangle(xMin, yMin, xMax, yMax, fill = fill, outline = outline)

class CellGrid(Canvas):
    def __init__(self, master, rowNumber, columnNumber, cellSize, *args, **kwargs):
        Canvas.__init__(self, master, width= cellSize * columnNumber, height = cellSize * rowNumber, *args, **kwargs)

        self.cellSize = cellSize

        self.grid=[]
        for row in range(rowNumber):
            line =[]
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize))

            self.grid.append(line)

        self.draw()
    
    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()