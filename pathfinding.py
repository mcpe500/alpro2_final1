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

def findpath(maze, x=None, y=None):
    if x is None and y is None:
        y, x = findstart(maze)

    path = []  # Variable to store the final path
    if backtrack(maze, x, y, path):
        path.reverse()  # Reverse the path to get the correct order
        return path
    else:
        return []

def backtrack(maze, x, y, path):
    if maze[y][x] == 99:
        return True

    if maze[y][x] != 10 and maze[y][x] != 99:
        maze[y][x] = 3  # Mark the current square as visited

    possible_moves = get_possible_moves(maze, x, y)
    for move in possible_moves:
        new_x = x + move[0]
        new_y = y + move[1]
        if backtrack(maze, new_x, new_y, path):
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


# def findpath(maze,x=None,y=None,path=None, found=False):
#     if x == None and y == None:
#         y,x = findstart(maze)
#     if path == None:
#         path = []
#     if maze[x][y] == 99 or found:
#         found = True
#         return path
#     if maze[x][y] == 0:
#         maze[x][y] = 3
#     if validMove(maze, x-1, y):
#         path.append((-1,0))
#         findpath(maze, x-1, y, path, found)

#     if validMove(maze, x+1, y):
#         path.append((1,0))
#         findpath(maze, x+1, y, path), found

#     if validMove(maze, x, y-1):
#         path.append((0,-1))
#         findpath(maze, x, y-1, path, found)

#     if validMove(maze, x, y+1):
#         path.append((0,1))
#         findpath(maze, x, y+1, path, found)

#     return path

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
    print(path)
    sY,sX = findstart(maze)
    eY,eX = findend(maze)
    for index in range(len(path)):
        pX,pY = path[index]
        if maze[sY+pY][sX+pX] != 1 and maze[sY+pY][sX+pX] != 99:
            maze[sY+pY][sX+pX] = 4
            sY += pY
            sX += pX
    return maze
    