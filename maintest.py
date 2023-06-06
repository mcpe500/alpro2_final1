import read_file
import generateMap
import pathfinding
import copy
import numpy as np
from concurrent.futures import ThreadPoolExecutor

def process_map(map, health, bestScore, bestMap, paths):
    temp = copy.deepcopy(map)
    tempPath, tempHist, tempSc, tempHp = pathfinding.findpath(temp, health)
    if tempSc > bestScore:
        bestScore = tempSc
        paths = np.array([tempPath, tempHist, tempSc, tempHp], dtype=object)
        bestMap = temp
    return bestScore, bestMap, paths

map, state = read_file.readMap("map")

if not state:
    map = generateMap.randomMap(map, 0, 0)
    map = generateMap.newMaze(map, 15, 3)
paths = np.array([0, 0, 0, 0], dtype=object)

health = 10

bestMap = copy.deepcopy(map)
bestScore = 0

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = []
    for i in range(1000):
        future = executor.submit(process_map, map, health, bestScore, bestMap, paths)
        futures.append(future)
        
    for future in futures:
        tempBestScore, tempBestMap, tempPaths = future.result()

        if tempBestScore > bestScore:
            bestScore = tempBestScore
            paths = tempPaths
            bestMap = tempBestMap
    # print(futures[0])

map = bestMap
path, history, score, health = paths

map = pathfinding.finalMaze(map, path)
history.append(np.array(map))
import visualize
visualize.animate(history, health, score)
