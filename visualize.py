import turtle
import time
import winsound


turtle.addshape("Wall.gif")
turtle.addshape("stonefloor.gif")
turtle.addshape("bestpath.gif")
turtle.addshape("pathed.gif")
turtle.addshape("start.gif")
turtle.addshape("exit.gif")
turtle.addshape("beartrap.gif")
turtle.addshape("lava.gif")
turtle.addshape("pathed_beartrap.gif")
turtle.addshape("bestpath_beartrap.gif")

p = turtle.Turtle()
def drawMaze(maze, size, health, score):
    start_x = -((len(maze[0]) * size) / 2)
    start_y = (len(maze) * size) / 2
    p.penup()
    p.goto(start_x, start_y)
    p.speed(0)
    p.hideturtle()
    p.getscreen().tracer(0)
    font_size = 16
    font_style = ("Arial", font_size, "normal")

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 0:
                # print("stonefloor")
                p.shape("stonefloor.gif")
            elif maze[i][j] == 1:
                # print("wall")
                p.shape("Wall.gif")
            elif maze[i][j] == 3:
                # print("pathed")
                p.shape("pathed.gif")
            elif maze[i][j] == 4:
                # print("bestpath")
                p.shape("bestpath.gif")
            elif maze[i][j] == 6:
                # print("beartrap")
                p.shape("beartrap.gif")
            elif maze[i][j] == 7:
                # print("lava")
                p.shape("lava.gif")
            elif maze[i][j] == 8:
                # print("pathed_beartrap")
                p.shape("pathed_beartrap.gif")
            elif maze[i][j] == 9:
                # print("bestpath_beartrap")
                p.shape("bestpath_beartrap.gif")
            elif maze[i][j] == 10:
                # print("start")
                p.shape("start.gif")
            elif maze[i][j] == 99:
                # print("exit")
                p.shape("exit.gif")
            
            p.stamp()
            p.forward(size)

        p.setpos(start_x, start_y - (i+1)*size)

    # Write health at top left
    health_x = start_x - 15
    health_y = start_y + size
    p.goto(health_x, health_y)
    p.write("Health: " + str(health), align="left", font=font_style)

    # Write score at top right
    score_x = start_x + len(maze[0]) * size - 15
    score_y = start_y + size
    p.goto(score_x, score_y)
    p.write("Score: " + str(score), align="right", font=font_style)
 

def clear():
    p.clear()

def update():
    p.getscreen().update()

def stop():
    turtle.done()

def animate(history, health, score):
    winsound.PlaySound("footsteps.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    for maze in history:
        clear()
        drawMaze(maze, 32, health, score)
        update()
        time.sleep(0.01)
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("Victory Music.wav", winsound.SND_FILENAME)
    stop()
