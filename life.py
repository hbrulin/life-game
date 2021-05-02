#TODO : Draw the initial alive cells on start
#TODO : attch buttons to keys

from tkinter import *
from random import randrange

height = 30
width = 30
side = 15 
alive = 1
dead = 0
running = False
speed = 100
it = 0

cell = [[0 for row in range(height)] for col in range(width)]
state = [[dead for row in range(height)] for col in range(width)]
temp = [[dead for row in range(height)] for col in range(width)]

def button_init():
    first_line_top = Frame(root)
    first_line_bottom = Frame(root)
    first_line_top.pack(side=TOP)
    first_line_bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

    start_btn = Button(root, text = 'Start', fg='green', command = start)
    start_btn.pack(in_=first_line_top, side=LEFT)

    stop_btn = Button(root, text = 'Stop', fg='red', command = stop)
    stop_btn.pack(in_=first_line_top, side=LEFT)

    step_btn = Button(root, text = 'Step', fg='blue', command = step)
    step_btn.pack(in_=first_line_top, side=LEFT)

    speed_btn = Button(root, text = 'Speed', fg='yellow', command = speed_up)
    speed_btn.pack(in_=first_line_top, side=LEFT)

    slow_btn = Button(root, text = 'Slow', fg='orange', command = slow_down)
    slow_btn.pack(in_=first_line_top, side=LEFT)

    second_line_top = Frame(root)
    second_line_bottom = Frame(root)
    second_line_top.pack(side=TOP)
    second_line_bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

    clear_btn = Button(root, text = 'Stop and clear', fg='dark red', command=lambda:[stop(),init()])
    clear_btn.pack(in_=second_line_top, side=LEFT)

    random_btn = Button(root, text = 'Randomize', fg='purple', command = randomize)
    random_btn.pack(in_=second_line_top, side=LEFT)

    close_btn = Button(root, text = 'Close', command = root.destroy)
    close_btn.pack()

def step():
    global it
    it += 1
    label.config(text=it)
    calculate()
    draw()

def stop():
    global running
    running = False

def start():
    global running
    running = True
    recursive()    

def speed_up():
    global speed
    speed -= 10

def slow_down():
    global speed
    speed += 10  

def recursive():
    if running:
        step()
    root.after(speed, recursive)

def randomize():
    init()
    for i in range(width*height//4):
        state[randrange(width)][randrange(height)] = alive
    draw()    

def init():
    for y in range(height):
        for x in range(width):
            state[x][y] = dead
            temp[x][y] = dead
            cell[x][y] = canvas.create_rectangle((x*side, y*side,
            (x+1)*side, (y+1)*side), outline="gray", fill="white") # create_rectangle method takes 4 coordinates: canvas.create_rectangle(x1, y1, x2, y2, **kwargs), with (x1,y1) the coordinates of the top left corner and (x2, y2) those of the bottom right corner. 

def calculate():
    for y in range(height):
        for x in range(width):
            # Rule 1 - Death by solitude
            if state[x][y] == alive and getNeighbors(x,y) < 2:
                temp[x][y] = dead
            # Rule 2 - Survival if 2 or 3 neighbors
            #if state[x][y] == alive and (getNeighbors(x,y) == 2 or getNeighbors(x,y) == 3):
            #    temp[x][y] = alive
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

root = Tk()
root.title("Conway Life Game")
label=Label(root,text=it)
label.pack(side=TOP, anchor=NW)

canvas = Canvas(root, width=side*width, height=side*height, highlightthickness=0)
canvas.pack()
button_init()
init()
root.mainloop()