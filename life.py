#TODO : Make start, stop, step by step, accelerate, slow buttons
#TODO : Draw the initial alive cells on start

from tkinter import *
from random import randrange

height = 30
width = 30
side = 15 
alive = 1
dead = 0

cell = [[0 for row in range(height)] for col in range(width)]
state = [[dead for row in range(height)] for col in range(width)]
temp = [[dead for row in range(height)] for col in range(width)]

def recursive():
 calculate()
 draw()
 window.after(100, recursive)

def init():
 for y in range(height):
    for x in range(width):
        state[x][y] = dead
        temp[x][y] = dead
        cell[x][y] = canvas.create_rectangle((x*side, y*side,
        (x+1)*side, (y+1)*side), outline="gray", fill="white") # create_rectangle method takes 4 coordinates: canvas.create_rectangle(x1, y1, x2, y2, **kwargs), with (x1,y1) the coordinates of the top left corner and (x2, y2) those of the bottom right corner. 
# randomise initial alive cells - CHANGE WITH POSSIBILITY TO DRAW THEM.
 for i in range(width*height//4):
    state[randrange(width)][randrange(height)] = alive

def calculate():
 for y in range(height):
    for x in range(width):
        # Rule 1 - Death by solitude
        if state[x][y] == alive and getNeighbors(x,y) < 2:
            temp[x][y] = dead
        # Rule 2 - Survival if 2 or 3 neighbors
        if state[x][y] == alive and (getNeighbors(x,y) == 2 or getNeighbors(x,y) == 3):
            temp[x][y] = alive
        # Rule 3 - Death by asphyxia
        if state[x][y] == alive and getNeighbors(x,y) > 3:
            temp[x][y] = dead
        # Rule 4 - Birth
        if state[x][y] == dead and getNeighbors(x,y) == 3:
            temp[x][y] = alive
 for y in range(height):
    for x in range(width):
        state[x][y] = temp[x][y]

def getNeighbors(x,y):
 res = 0
 if state[(x-1)%width][(y+1)%height] == alive:
    res += 1
 if state[x][(y+1)%height] == alive:
    res += 1
 if state[(x+1)%width][(y+1)%height] == alive:
    res += 1
 if state[(x-1)%width][y] == alive:
    res += 1
 if state[(x+1)%width][y] == alive:
    res += 1
 if state[(x-1)%width][(y-1)%height] == alive:
    res += 1
 if state[x][(y-1)%height] == alive:
    res += 1
 if state[(x+1)%width][(y-1)%height] == alive:
    res += 1
 return res

def draw():
 for y in range(height):
    for x in range(width):
        if state[x][y]== dead:
            color = "white"
        else:
            color = "blue"
        canvas.itemconfig(cell[x][y], fill=color)

window = Tk()
window.title("Conway Life Game")
canvas = Canvas(window, width=side*width, height=side*height, highlightthickness=0)
canvas.pack()
init()
recursive()
window.mainloop()