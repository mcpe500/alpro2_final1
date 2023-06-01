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

def findpath(maze,x=None,y=None,path=None):
    if x == None and y == None:
        y,x = findstart(maze)
    if path == None:
        path = []
    possible_moves = []
    if x > 0:
        possible_moves.append((-1,0))
    if x < len(maze[0])-1:
        possible_moves.append((1,0))
    if y > 0:
        possible_moves.append((0,-1))
    if y < len(maze)-1:
        possible_moves.append((0,1))
    for move in possible_moves:
        if (maze[y+move[1]][x+move[0]] == 0 or maze[y+move[1]][x+move[0]] == 99) and maze[y+move[1]][x+move[0]] != 3:
            if maze[y][x] != 10 and maze[y][x] != 99:
                maze[y][x] = 3
            path.append(move)
            findpath(maze,x+move[0],y+move[1],path)
    return path

def finalMaze(maze,path):
    print(path)
    sY,sX = findstart(maze)
    # eY,eX = findend(maze)
    index = len(path)-1
    while index >= 0:
        pX,pY = path[index]
        if maze[sY+pY][sX+pX] == 3:
            maze[sY+pY][sX+pX] = 4
            sY += pY
            sX += pX
        index -= 1
    return maze
    