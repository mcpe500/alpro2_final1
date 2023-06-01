import turtle

def box(pen, size):
    pen.shape("Wall.gif")
    pen.shapesize(0.01)  # adjust the size of the turtle shape based on the size of the maze cell
    pen.stamp()

def drawMaze(maze, size):
    turtle.addshape("Wall.gif")
    turtle.addshape("stonefloor.gif")
    turtle.addshape("bestpath.gif")
    turtle.addshape("pathed.gif")
    turtle.addshape("exit.gif")
    p = turtle.Turtle()
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
                # p.color("white")
                p.shape("stonefloor.gif")
            elif maze[i][j] == 1:
                # p.color("black")
                p.shape("Wall.gif")
            elif maze[i][j] == 3:
                # p.color("grey")
                p.shape("pathed.gif")
            elif maze[i][j] == 4:
                # p.color("cyan")
                p.shape("bestpath.gif")
            elif maze[i][j] == 10:
                p.color("green")
            elif maze[i][j] == 99:
                # p.color("red")
                p.shape("exit.gif")
            p.shapesize(1)  # adjust the size of the turtle shape based on the size of the maze cell
            p.stamp()
            # box(p, size)
            p.forward(size)
        p.setpos(start_x, start_y - (i+1)*size)
    turtle.done()
