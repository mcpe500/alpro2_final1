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
        if maze[y+move[1]][x+move[0]] == 0 and (y+move[1],x+move[0]) not in path:
            if maze[y][x] != 10:
                maze[y][x] = 3
                path.append(move)
            findpath(maze,x+move[0],y+move[1],path)
    return path

def finalMaze(maze,path):
    print(path)
    sY,sX = findstart(maze)
    # eY,eX = findend(maze)
    for pX,pY in path:
        if maze[sY+pY][sX+pX] == 3:
            maze[sY+pY][sX+pX] = 4
            sY += pY
            sX += pX
    return maze
    