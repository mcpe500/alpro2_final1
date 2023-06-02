import copy
import random

def findstart(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 10:
                return i, j
def findend(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 99:
                return i, j

def findpath(maze, x=None, y=None, history=None):
    if x is None and y is None:
        y, x = findstart(maze)
    if history is None:
        history = []
    path = []  # Variable to store the final path
    health = 0

    isValid, health = backtrack(maze, x, y, path, 10, history)
    if isValid:
        path.reverse()  # Reverse the path to get the correct order
        # score = round((2*(1/len(path)))*(1*health))
        score = round(((1000-len(path))*1)*(health*0.5))
        return path, history, score, health
    else:
        return [], history, 0, 0

def backtrack(maze, x, y, path, health, history):
    if maze[y][x] == 99:
        return True, health

    if maze[y][x] == 0:
        maze[y][x] = 3  # Mark the current square as visited
    elif maze[y][x] == 6:
        maze[y][x] = 8
        health -= 1

    possible_moves = getPossibleMoves(maze, x, y, health)
    random.shuffle(possible_moves)

    for move in possible_moves:
        new_x = x + move[0]
        new_y = y + move[1]
        history.append(copy.deepcopy(maze))
        isValid, newHealth = backtrack(maze, new_x, new_y, path, health, history)
        if isValid:
            path.append(move)
            health = newHealth
            return True, health
        
    if maze[y][x] == 8:
        health += 1  # Increment health if backtracking from a previously visited square with health penalty

    return False, health

def getPossibleMoves(maze, x, y, health):
    moves = []
    if x > 0 and (maze[y][x-1] == 0 or (maze[y][x-1] == 6 and health-1>=0) or maze[y][x-1] == 99):
        moves.append((-1, 0))
    if x < len(maze[0]) - 1 and (maze[y][x+1] == 0 or (maze[y][x+1] == 6 and health-1>=0) or maze[y][x+1] == 99):
        moves.append((1, 0))
    if y > 0 and (maze[y-1][x] == 0 or (maze[y-1][x] == 6 and health-1>=0) or maze[y-1][x] == 99):
        moves.append((0, -1))
    if y < len(maze) - 1 and (maze[y+1][x] == 0 or (maze[y+1][x] == 6 and health-1>=0) or maze[y+1][x] == 99):
        moves.append((0, 1))
    return moves

def finalMaze(maze,path):
    # print(path)
    sY,sX = findstart(maze)
    for index in range(len(path)):
        pX,pY = path[index]
        if maze[sY+pY][sX+pX] == 3:
            maze[sY+pY][sX+pX] = 4
            sY += pY
            sX += pX
        elif maze[sY+pY][sX+pX] == 8:
            maze[sY+pY][sX+pX] = 9
            sY += pY
            sX += pX
    return maze
    