import read_file
import generateMap
import pathfinding
import copy
import numpy as np

map,state = read_file.readMap("map")

if not state:
    map = generateMap.randomMap(map, 0, 0)
    map = generateMap.newMaze(map, 15, 3)
paths = np.array([0,0,0,0])

health = 10

bestMap = copy.deepcopy(map)
bestScore = 0
for i in range(1000):
    temp = copy.deepcopy(map)
    tempPath, tempHist, tempSc, tempHp = pathfinding.findpath(temp,health)
    if tempSc>bestScore:
        print("percobaan ke",i)
        print(tempSc)
        bestScore = tempSc
        paths = np.array([tempPath, tempHist, tempSc, tempHp], dtype=object)
        # print(paths)
        # paths.append([tempPath, tempHist, tempSc, tempHp])
        bestMap = temp
map = bestMap
# path, history, score, health = paths[len(paths)-1]
path, history, score, health = paths
print(score)
# print(path)
map = pathfinding.finalMaze(map,path)
np.array(history.append(np.array(map)))
import visualize
visualize.animate(history, health, score)
