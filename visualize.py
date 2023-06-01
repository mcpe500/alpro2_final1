import turtle

def box(pen, int_dim):
    pen.begin_fill()
    
    # 0 deg.
    pen.forward(int_dim)
    pen.left(90)
    
    # 90 deg.
    pen.forward(int_dim)
    pen.left(90)
    
    # 180 deg.
    pen.forward(int_dim)
    pen.left(90)
    
    # 270 deg.
    pen.forward(int_dim)
    pen.end_fill()
    pen.setheading(0)

def drawMaze(maze, size):
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
                p.color("white")
            elif maze[i][j] == 1:
                p.color("black")
            elif maze[i][j] == 3:
                p.color("grey")
            elif maze[i][j] == 4:
                p.color("cyan")
            elif maze[i][j] == 10:
                p.color("green")
            elif maze[i][j] == 99:
                p.color("red")
            box(p, size)
            p.forward(size)
        p.setheading(270)
        p.penup()
        p.forward(size)
        p.setheading(180)
        p.forward(size * len(maze[0]))
        p.setheading(0)
        p.pendown()
    turtle.done()
