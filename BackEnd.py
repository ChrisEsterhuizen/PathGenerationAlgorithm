import turtle   #import turtle library
import time
import sys
from collections import deque

'''Setup the turtle graphics'''
wn = turtle.Screen()    #define the turtle screen
wn.bgcolor("black")     #define background colour of trurle screen
wn.title("A Breadth First Search Algorithm")
wn.setup(1300,700)      #define the dimensions of turtle window

'''Class for turtle window maze'''
class Maze(turtle.Turtle):      #define class Maze
    def __init__(self):     #constructor
        turtle.Turtle.__init__(self)
        self.shape("square")        #define the turtle block shape
        self.color("white")         #define the colour of the turtle squares
        self.penup()                #lift up the drawing pen do it does not leave a trail
        self.speed(0)

'''Class for drawing the solved path line - green line in maze'''
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

'''Class for drawing the end point'''
class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

'''Class for drawing the starting point'''
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

'''Class for the drawing of the backtracking path'''
class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

'''The maze to be drawn'''
grid1 = [
"+++++++++++++++",
"+            e+",
"+             +",
"+             +",
"+             +",
"+             +",
"+             +",
"+             +",
"+ s           +",
"+++++++++++++++",
]

grid = [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+               +                                 +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+s          +                 +               ++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++e ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +     +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++ +++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]
'''Function for drawing the maze using grid layout'''
def setup_maze(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 -(y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)       #move drawing pen to the set x and y location and
                maze.stamp()                        #stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))  #add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))     #add " " and e to path list

            if character == "e":
                green.color("blue")
                green.goto(screen_x, screen_y)      #send green sprite to screen location
                end_x, end_y = screen_x, screen_y   #assign end location's location coordinates to end_x and end_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y # assign the start location variables to where on the turtle screen an "s" is found
                red.goto(screen_x, screen_y)

def endProram():
    wn.exitonclick()
    sys.exit()

'''Function of breadth first search algorithm'''
def search(x,y):
    frontier.append((x, y))          #load starting square location in frontier list
    solution[x, y] = x, y             #the current cell it is in is x, y

    while len(frontier) > 0:        #check if there are value in the frontier list and exit when there is none
        time.sleep(0)
        x, y = frontier.popleft()   #remove the previous entry out of the frontier list and place the next entry in the frontier queue to the current x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:       #check whether square cell to the left has been visited
            cell = (x - 24, y)      #the cell being looked at
            solution[cell] = x, y   #for the backtracking; the parent coordinatres for the cell being lloked at is the current x, y values // for the cell as key; log the cuurrent cell loking at it
            frontier.append(cell)   #after identifng the cell as a unsearched cell at move it into the frontier list
            visited.add((x - 24, y))

        if(x, y - 24) in path and (x, y - 24) not in visited:       #check whether bottom square cell has been visited
            cell = (x, y - 24)      #the cell being looked at
            solution[cell] = x, y   #for the backtracking; the parent coordinatres for the cell being lloked at is the current x, y values // for the cell as key; log the cuurrent cell loking at it
            frontier.append(cell)   #after identifng the cell as a unsearched cell at move it into the frontier list
            visited.add((x, y - 24))

        if (x + 24, y) in path and (x + 24, y) not in visited:  # check whether square cell to the right has been visited
            cell = (x + 24, y)      #the cell being looked at
            solution[cell] = x, y   #for the backtracking; the parent coordinatres for the cell being lloked at is the current x, y values // for the cell as key; log the cuurrent cell loking at it
            frontier.append(cell)   #after identifng the cell as a unsearched cell at move it into the frontier list
            visited.add((x + 24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:       #check whether top square cell has been visited
            cell = (x, y + 24)      #the cell being looked at
            solution[cell] = x, y   #for the backtracking; the parent coordinatres for the cell being lloked at is the current x, y values // for the cell as key; log the cuurrent cell loking at it
            frontier.append(cell)   #after identifng the cell as a unsearched cell at move it into the frontier list
            visited.add((x, y + 24))

        green.goto(x, y)    #after inspecting the surrounding cells; move the drawing pen te the current location an
        green.stamp()       #stamp the location with a green stamp to indicated it has been searched

'''Function for backtarcking algorithm'''
def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):     #stop the back tracking when current cell is the start cell
        yellow.goto(solution[x, y])         #move the yellow drawing pen to the solution path and stamp it yellow
        yellow.stamp()
        x, y = solution[x, y]               #the "key value" becomes the new key

# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}

# main program starts here ####
setup_maze(grid)
search(start_x, start_y)
backRoute(end_x, end_y)
wn.exitonclick()
print("Jasmina")