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

def findpath(maze, x=None, y=None,history=None,prevScore=None):
    distance = 0
    if x is None and y is None:
        y, x = findstart(maze)
    if history is None:
        history = []
    if prevScore is None:
        prevScore = 0
    path = []  # Variable to store the final path
    if backtrack(maze, x, y, path, history):
        path.reverse()  # Reverse the path to get the correct order
        score = 1000-len(path)
        if score < prevScore:
            return None,None,None
        return path, history, score
    else:
        return [], history, 0

def backtrack(maze, x, y, path, history):
    if maze[y][x] == 99:
        return True

    if maze[y][x] != 10 and maze[y][x] != 99:
        maze[y][x] = 3  # Mark the current square as visited

    possible_moves = get_possible_moves(maze, x, y)
    random.shuffle(possible_moves)
    for move in possible_moves:
        new_x = x + move[0]
        new_y = y + move[1]
        history.append(copy.deepcopy(maze))
        if backtrack(maze, new_x, new_y, path, history):
            path.append(move)
            return True
    return False

def get_possible_moves(maze, x, y):
    moves = []
    if x > 0 and (maze[y][x-1] == 0 or maze[y][x-1] == 99):
        moves.append((-1, 0))
    if x < len(maze[0]) - 1 and (maze[y][x+1] == 0 or maze[y][x+1] == 99):
        moves.append((1, 0))
    if y > 0 and (maze[y-1][x] == 0 or maze[y-1][x] == 99):
        moves.append((0, -1))
    if y < len(maze) - 1 and (maze[y+1][x] == 0 or maze[y+1][x] == 99):
        moves.append((0, 1))
    return moves


# def finalMaze(maze,path):
#     print(path)
#     sY,sX = findstart(maze)
#     # eY,eX = findend(maze)
#     index = len(path)-1
#     while index >= 0:
#         pX,pY = path[index]
#         if maze[sY+pY][sX+pX] == 3:
#             maze[sY+pY][sX+pX] = 4
#             sY += pY
#             sX += pX
#         elif maze[sY+pY][sX+pX] == 99:
#             return maze
#         index -= 1
#     return maze

def finalMaze(maze,path):
    # print(path)
    sY,sX = findstart(maze)
    for index in range(len(path)):
        pX,pY = path[index]
        if maze[sY+pY][sX+pX] != 1 and maze[sY+pY][sX+pX] != 99:
            maze[sY+pY][sX+pX] = 4
            sY += pY
            sX += pX
    return maze
    