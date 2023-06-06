import random
import sys

sys.setrecursionlimit(100000)

def createEmptyMap(width, height):
    return [[1] * width for _ in range(height)]

# def isAllVisited(visited):
#     for i in visited:
#         for j in i:
#             if not j:
#                 return False
#     return True

# def isStuck(visited, yx, wall):
#     temp = visited.copy()
#     for i in wall:
#         if (yx[0] + i[0] < 0 or yx[0] + i[0] >= len(visited) or yx[1] + i[1] < 0 or yx[1] + i[1] >= len(visited[0])):
#             continue
#         else:
#             temp[yx[0] + i[0]][yx[1] + i[1]] = True
    
#     if not isAllVisited(temp):
#         if yx[0] == 0:
#             if not temp[yx[0]+1][yx[1]]:
#                 return True
#         elif yx[0] == len(temp)-1:
#             if not temp[yx[0]-1][yx[1]]:
#                 return True
#         elif yx[1] == 0:
#             if not temp[yx[0]][yx[1]+1]:
#                 return True
#         elif yx[1] == len(temp[0])-1:
#             if not temp[yx[0]][yx[1]-1]:
#                 return True
#         else:
#             if not temp[yx[0]+1][yx[1]] and not temp[yx[0]-1][yx[1]] and not temp[yx[0]][yx[1]+1] and not temp[yx[0]][yx[1]-1]:
#                 return True
#     return False

# def depth_first_search_map(x, y, maze):
#     maze[y][x] = 0
#     possible = [[0, 2], [2, 0], [0, -2], [-2, 0]]
#     random.shuffle(possible)
#     for x1, y1 in possible:
#         lx1, ly1 = x + x1, y + y1
#         if 0 <= lx1 < len(maze[0]) and 0 <= ly1 < len(maze) and maze[ly1][lx1] == 1:
#             maze[y + y1 // 2][x + x1 // 2] = 0
#             depth_first_search_map(lx1, ly1, maze)

def randomMap(maze, x, y,visited=None):
    maze[y][x] = 0
    if visited == None:
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cover = [
        [(1, 0), (-1, 0)],
        [(0, 1), (0, -1)],
    ]
    random.shuffle(moves)
    for moveX, moveY in moves:
        next_moveX = x + moveX
        next_moveY = y + moveY
        if (next_moveX >= 0 and next_moveX < len(maze[0]) and next_moveY >= 0 and next_moveY < len(maze)):
            if maze[next_moveY][next_moveX] == 1 and not visited[next_moveY][next_moveX]:
                maze[y+moveY][x+moveX] = 0
                wall = []
                if(moveX,moveY) == moves[0]:
                    wall = cover[0]
                elif(moveX,moveY) == moves[1]:
                    wall = cover[1]
                elif(moveX,moveY) == moves[2]:
                    wall = cover[0]
                elif(moveX,moveY) == moves[3]:
                    wall = cover[1]
                wall1X,wall1Y = wall[0]
                wall2X,wall2Y = wall[1]
                if (next_moveX + wall1X >= 0 and next_moveX + wall1X < len(maze[0]) and next_moveY + wall1Y >= 0 and next_moveY + wall1Y < len(maze)):
                    visited[next_moveY + wall1Y][next_moveX + wall1X] = True
                if (next_moveX + wall2X >= 0 and next_moveX + wall2X < len(maze[0]) and next_moveY + wall2Y >= 0 and next_moveY + wall2Y < len(maze)):
                    visited[next_moveY + wall2Y][next_moveX + wall2X] = True
                randomMap(maze, next_moveX, next_moveY,visited)
    return maze
    
def validLava(maze, x, y):
    empty = 0
    if x-1 >= 0 and maze[y][x-1] == 0:
        empty += 1
    if x+1 < len(maze[0]) and maze[y][x+1] == 0:
        empty += 1
    if y-1 >= 0 and maze[y-1][x] == 0:
        empty += 1
    if y+1 < len(maze) and maze[y+1][x] == 0:
        empty += 1
    return (empty >= 2) and maze[y][x] == 1


def newMaze(maze, trapCount, lavaCount):
    nMaze = []
    for i in range(len(maze)):
        nMaze.append([])
        for j in range(len(maze[i])):
            nMaze[i].append(maze[i][j])

    for i in range(1, 4):
        for j in range(1, 4):
            nMaze[i][j] = 0
    nMaze[1][1] = 10
    y,x = random.randint(len(maze)//2,len(maze)-1),random.randint(len(maze[0])//2,len(maze[0])-1)
    while True:
        if nMaze[y][x] == 0:
            nMaze[y][x] = 99
            break
        else:
            y,x = random.randint(len(maze)//2,len(maze)-1),random.randint(len(maze[0])//2,len(maze[0])-1)

    for i in range(0, trapCount):
        y,x = random.randint(0,len(maze)-1),random.randint(0,len(maze[0])-1)
        while nMaze[y][x] != 0:
            y,x = random.randint(0,len(maze)-1),random.randint(0,len(maze[0])-1)
        nMaze[y][x] = 6

    for i in range(0, lavaCount):
        y,x = random.randint(0,len(maze)-1),random.randint(0,len(maze[0])-1)
        while not validLava(maze, x, y):
            y,x = random.randint(0,len(maze)-1),random.randint(0,len(maze[0])-1)
        nMaze[y][x] = 7

    return nMaze

# def randomMap(maze):
#     kolom = len(maze)
#     baris = len(maze[0])
#     nMaze = [[1] * baris for _ in range(kolom)]
#     nVisited = [[False] * baris for _ in range(kolom)]
#     start_yx = (0, 0)
#     cover = [
#         [(1, 0), (-1, 0)],
#         [(0, 1), (0, -1)],
#     ]
#     prev = []
#     while True:
#         moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         if start_yx[0] == 0 and start_yx[1] == 0:
#             moves = [(0, 1), (1, 0)]
#         elif start_yx[0] == 0 and start_yx[1] == baris - 1:
#             moves = [(0, -1), (1, 0)]
#         elif start_yx[0] == kolom - 1 and start_yx[1] == 0:
#             moves = [(0, 1), (-1, 0)]
#         elif start_yx[0] == kolom - 1 and start_yx[1] == baris - 1:
#             moves = [(0, -1), (-1, 0)]
#         elif start_yx[0] == 0:
#             moves = [(0, 1), (0, -1), (1, 0)]
#         elif start_yx[0] == kolom - 1:
#             moves = [(0, 1), (0, -1), (-1, 0)]
#         elif start_yx[1] == 0:
#             moves = [(0, 1), (1, 0), (-1, 0)]
#         elif start_yx[1] == baris - 1:
#             moves = [(0, -1), (1, 0), (-1, 0)]
#         nMaze[start_yx[0]][start_yx[1]] = 0
#         nVisited[start_yx[0]][start_yx[1]] = True
#         move = random.randint(0, len(moves) - 1)
#         next_move = moves[move]
#         next_yx = (start_yx[0] + next_move[0], start_yx[1] + next_move[1])
#         if (next_yx[0] < 0 or next_yx[0] >= kolom or next_yx[1] < 0 or next_yx[1] >= baris):
#             continue
#         if nVisited[next_yx[0]][next_yx[1]]:
#             continue
#         nMaze[next_yx[0]][next_yx[1]] = 0
#         nVisited[next_yx[0]][next_yx[1]] = True
#         wall = cover[move % 2]
#         if isStuck(nVisited, next_yx,wall):
#             continue
#         for i in wall:
#             if (start_yx[0] + i[0] < 0 or start_yx[0] + i[0] >= kolom or start_yx[1] + i[1] < 0 or start_yx[1] + i[1] >= baris):
#                 continue
#             else:
#                 nVisited[start_yx[0] + i[0]][start_yx[1] + i[1]] = True
#         if isAllVisited(nVisited):
#             break
#         prev.append({"previous":start_yx,"next_move":next_move})
#         start_yx = next_yx

#     return nMaze
