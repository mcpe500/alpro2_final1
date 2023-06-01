import read_file
import generateMap
import pathfinding
import copy

map,state = read_file.readMap("map")
map = generateMap.randomMap(map, 0, 0)

if not state:
    map = generateMap.newMaze(map)
paths = []

for i in range(100):
    temp = copy.deepcopy(map)
    paths.append(pathfinding.findpath(temp))

bestScore = 0
index = -1
for i in range(len(paths)):
    path, history, score = paths[i]
    print(score)
    if (score>bestScore):
        bestScore = score
        index = i

path, history, score = paths[index]
print(bestScore)

# path, history, score = pathfinding.findpath(map)

map = pathfinding.finalMaze(map,path)
history.append(map)
# for i in map:
#     print(i)

# for i in history:
#     print(i)
import visualize
visualize.animate(history)


