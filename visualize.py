import turtle

turtle.addshape("Wall.gif")
turtle.addshape("stonefloor.gif")
turtle.addshape("bestpath.gif")
turtle.addshape("pathed.gif")
turtle.addshape("exit.gif")

p = turtle.Turtle()

def box(pen, size):
    pen.shape("Wall.gif")
    pen.shapesize(0.01)  # adjust the size of the turtle shape based on the size of the maze cell
    pen.stamp()

def drawMaze(maze, size):
    start_x = -((len(maze[0]) * size) / 2)
    start_y = (len(maze) * size) / 2
    p.penup()
    p.goto(start_x, start_y)
    p.speed(0)
    p.hideturtle()
    p.getscreen().tracer(0)

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 0:
                print("stonefloor")
                p.shape("stonefloor.gif")
            elif maze[i][j] == 1:
                print("wall")
                p.shape("Wall.gif")
            elif maze[i][j] == 3:
                print("pathed")
                p.shape("pathed.gif")
            elif maze[i][j] == 4:
                print("bestpath")
                p.shape("bestpath.gif")
            elif maze[i][j] == 10:
                print("start")
                p.color("green")
            elif maze[i][j] == 99:
                print("end")
                p.shape("exit.gif")
            
            p.shapesize(stretch_wid=size/20, stretch_len=size/20)
            p.stamp()
            p.forward(size)

        p.setpos(start_x, start_y - (i+1)*size)

def clear():
    p.clear()

def update():
    p.getscreen().update()

def stop():
    turtle.done()
