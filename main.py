import read_file
import generateMap
import pathfinding
import copy

map,state = read_file.readMap("map")
map = generateMap.randomMap(map, 0, 0)

if not state:
    map = generateMap.newMaze(map, 15, 3)
paths = []

bestMap = copy.deepcopy(map)
bestScore = 0
for i in range(500):
    temp = copy.deepcopy(map)
    tempPath, tempHist, tempSc = pathfinding.findpath(temp)
    if tempSc>=bestScore:
        print(tempSc)
        bestScore = tempSc
        paths.append([tempPath, tempHist, tempSc])
        bestMap = temp

map = bestMap
path, history, score = paths[len(paths)-1]
print(score)


# path, history, score = pathfinding.findpath(map)

map = pathfinding.finalMaze(map,path)
history.append(map)
# for i in map:
#     print(i)

# for i in history:
#     print(i)
import visualize
visualize.animate(history)
