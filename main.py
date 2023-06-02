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
for i in range(1000):
    temp = copy.deepcopy(map)
    tempPath, tempHist, tempSc, tempHp = pathfinding.findpath(temp)
    if tempSc>=bestScore:
        print(tempSc)
        bestScore = tempSc
        paths.append([tempPath, tempHist, tempSc, tempHp])
        bestMap = temp

map = bestMap
path, history, score, health = paths[len(paths)-1]
print(score)

map = pathfinding.finalMaze(map,path)
history.append(map)
# for i in map:
#     print(i)

# for i in history:
#     print(i)
import visualize
visualize.animate(history, health, score)
