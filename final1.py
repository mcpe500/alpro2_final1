import turtle
import random

myPen = turtle.Turtle()
myPen.speed(0)
myPen.hideturtle()
myPen.getscreen().tracer(0)

targets = []

def text(message, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)
    myPen.write(message, align="left", font=FONT)

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)


palette = ["#FFFFFF", "#000000", "#00ff00", "#ff00ff", "#AAAAAA", "#FFFF00"]


def create_map(w, h):
    return [[1 for _ in range(w)] for _ in range(h)]


def depth_first_search_map(x, y, maze):
    maze[y][x] = 0
    possible = [[0, 2], [2, 0], [0, -2], [-2, 0]]
    random.shuffle(possible)
    for x1, y1 in possible:
        lx1, ly1 = x + x1, y + y1
        if 0 <= lx1 < len(maze[0]) and 0 <= ly1 < len(maze) and maze[ly1][lx1] == 1:
            maze[y + y1 // 2][x + x1 // 2] = 0
            depth_first_search_map(lx1, ly1, maze)

def newMaze(maze, trap_count):
    rows, cols = len(maze)*2, len(maze[0])*2
    nmaze = [[1] * (cols + 2) for _ in range(rows + 2)]

    for i in range(rows):
        for j in range(cols):
            nmaze[i + 1][j + 1] = maze[i//2][j//2]

    for i in range(2, 5):
        for j in range(2, 5):
            nmaze[i][j] = 0

    for _ in range(trap_count):
        while True:
            i, j = random.randint(1, rows), random.randint(1, cols)
            if nmaze[i][j] == 0:
                nmaze[i][j] = 5
                break

    for i in range(rows - 2, rows + 1):
        for j in range(cols - 2, cols + 1):
            nmaze[i][j] = 0

    nmaze[rows - 1][cols - 1] = 2
    targets.append((rows - 1, cols - 1))

    return nmaze

def drawMaze(maze, current_health, best_path=[]):
    boxSize = 15
    start_x = -((len(maze[0]) * boxSize) / 2)
    start_y = (len(maze) * boxSize) / 2

    myPen.penup()
    myPen.goto(start_x, start_y)
    myPen.setheading(0)

    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if (row, col) in best_path:  # Reversed row and col indices
                myPen.color("#ADD8E6")  # Light blue color for best path
            else:
                myPen.color(palette[maze[row][col]])
            box(boxSize)
            myPen.forward(boxSize)

        myPen.setheading(270)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.setheading(180)
        myPen.forward(boxSize * len(maze[row]))
        myPen.setheading(0)
        myPen.pendown()

    text("Health: {}".format(current_health), start_x, start_y + 20, 14)

def exploreMaze(maze, row, col, targets, collected, health, visited, distance=0, best_score=0, best_path=[]):
    if (row, col) in visited:
        return False, best_score, best_path, health

    visited.add((row, col))

    if maze[row][col] in [2, 0]:
        if (row, col) in targets:
            targets.remove((row, col))
            collected.append((row, col))
            if not targets:
                print("Distance:", distance)
                score = distance * health * 0.1
                print("Score:", score)
                if score > best_score:
                    best_score = score
                    best_path = collected.copy()
                return True, best_score, best_path, health

        maze[row][col] = 3
        myPen.clear()
        drawMaze(maze, health, best_path)
        myPen.getscreen().update()

        neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        for neighbor in neighbors:
            nrow, ncol = neighbor
            if 0 <= nrow < len(maze) and 0 <= ncol < len(maze[nrow]):
                if maze[nrow][ncol] != 5 or isAdjacentToTrap(maze, nrow, ncol):  # Check if neighbor is not a trap or adjacent to a trap
                    solved, best_score, best_path, health = exploreMaze(maze, nrow, ncol, targets, collected + [(row, col)], health, visited, distance + 1, best_score, best_path)
                    if solved:
                        return True, best_score, best_path, health

        maze[row][col] = 4
        myPen.clear()
        drawMaze(maze, health, best_path)
        myPen.getscreen().update()
        print("Backtrack")

    elif maze[row][col] == 5:
        if health > 50:
            health -= 50
            maze[row][col] = 4
            myPen.clear()
            drawMaze(maze, health, best_path)
            myPen.getscreen().update()

            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            valid_neighbors = []
            for neighbor in neighbors:
                nrow, ncol = neighbor
                if 0 <= nrow < len(maze) and 0 <= ncol < len(maze[nrow]):
                    if maze[nrow][ncol] != 5 or isAdjacentToTrap(maze, nrow, ncol):  # Check if neighbor is not a trap or adjacent to a trap
                        valid_neighbors.append(neighbor)

            if valid_neighbors:
                nrow, ncol = random.choice(valid_neighbors)
                solved, best_score, best_path, health = exploreMaze(maze, nrow, ncol, targets, collected + [(row, col)], health, visited, distance + 1, best_score, best_path)
                if solved:
                    return True, best_score, best_path, health

            health += 50
            maze[row][col] = 5
            myPen.clear()
            drawMaze(maze, health, best_path)
            myPen.getscreen().update()
            print("Backtrack from trap")

    return False, best_score, best_path, health



def isAdjacentToTrap(maze, row, col):
    neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
                 (row + 1, col + 1), (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1)]
    for neighbor in neighbors:
        nrow, ncol = neighbor
        if 0 <= nrow < len(maze) and 0 <= ncol < len(maze[nrow]) and maze[nrow][ncol] == 5:
            return True
    return False


def generateBestPath(best_path, maze):
    score = float('-inf')
    best_score = float('-inf')
    for i in range(len(best_path)-1, -1, -1):
        row, col = best_path[i]
        score += 1
        if maze[row][col] == 5:
            score -= 5
        elif maze[row][col] == 2:
            score += 10

        if score > best_score:
            best_score = score

    return best_score, best_path


maze = create_map(35, 20)
depth_first_search_map(1, 1, maze)
maze = newMaze(maze, 20)  # Adjust the target and trap counts as needed

drawMaze(maze, 100, [])
myPen.getscreen().update()

visited = set()
solved, _, best_path, health = exploreMaze(maze, 2, 2, targets, [], 100, visited)

if solved:
    print("Maze Solved")
    text("Maze Solved", -100, -150, 20)

    best_score, best_path = generateBestPath(best_path, maze)
    print("Best Path:", best_path)
    text("Best Path: {}".format(best_path), -130, -170, 16)

    
    print("Best Score:", best_score)
    text("Best Score: {}".format(best_score), -100, -190, 16)

    myPen.clear()
    drawMaze(maze, health, best_path)  # Redraw the maze with the best path and current health
    myPen.getscreen().update()

else:
    print("Cannot Solve Maze")
    text("Cannot Solve Maze", -130, -150, 20)

turtle.done()