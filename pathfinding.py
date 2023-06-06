import copy
import random
import numpy as np

def findstart(maze):
    for i in range(len(maze)):
        if isinstance(maze[i], np.int32):
            return i, np.where(maze[i] == 10)
        for j in range(len(maze[i])):
            if maze[i][j] == 10:
                return i, j
            
# import numpy as np

# def findstart(maze):
#     if isinstance(maze, np.int32):
#         return np.where(maze == 10)
#     elif isinstance(maze[0], np.ndarray) and isinstance(maze[0][0], np.int32):
#         return np.where(maze == 10)
#     else:
#         for i in range(len(maze)):
#             for j in range(len(maze[i])):
#                 if maze[i][j] == 10:
#                     return i, j




def findend(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 99:
                return i, j

def findpath(maze,health, x=None, y=None, history=None):
    if x is None and y is None:
        y, x = findstart(maze)
    if history is None:
        history = []
    path = []

    isValid, health = backtrack(maze, x, y, path, health, history)
    if isValid:
        path.reverse()
        # score = round((2*(1/len(path)))*(1*health))
        # path = np.array(path)
        score = round(((1000-len(path))*1)*(health*0.5))
        return path, history, score, health
    else:
        return [], history, 0, 0

def backtrack(maze, x, y, path, health, history):
    if maze[y][x] == 99:
        return True, health

    if maze[y][x] == 0:
        maze[y][x] = 3 
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
            path.append(np.array(move))
            health = newHealth
            return True, health
        
    if maze[y][x] == 8:
        health += 1 

    return False, health

def getPossibleMoves(maze, x, y, health):
    moves = []
    maze = np.array(maze, dtype=np.int8)
    if x > 0 and (maze[y, x-1] == 0 or (maze[y, x-1] == 6 and health-1 >= 0) or maze[y, x-1] == 99):
        moves.append(np.array([-1, 0], dtype=np.int8))
    if x < maze.shape[1] - 1 and (maze[y, x+1] == 0 or (maze[y, x+1] == 6 and health-1 >= 0) or maze[y, x+1] == 99):
        moves.append(np.array([1, 0], dtype=np.int8))
    if y > 0 and (maze[y-1, x] == 0 or (maze[y-1, x] == 6 and health-1 >= 0) or maze[y-1, x] == 99):
        moves.append(np.array([0, -1], dtype=np.int8))
    if y < maze.shape[0] - 1 and (maze[y+1, x] == 0 or (maze[y+1, x] == 6 and health-1 >= 0) or maze[y+1, x] == 99):
        moves.append(np.array([0, 1], dtype=np.int8))
    return moves

def finalMaze(maze, path):
    sY, sX = findstart(maze)
    print(path)
    path_length = len(path) 
    for index in range(path_length):
        pX, pY = path[index]
        if maze[sY + pY][sX + pX] == 3:
            maze[sY + pY][sX + pX] = 4
            sY += pY
            sX += pX
        elif maze[sY + pY][sX + pX] == 8:
            maze[sY + pY][sX + pX] = 9
            sY += pY
            sX += pX
    return maze

    