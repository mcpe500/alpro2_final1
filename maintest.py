import concurrent.futures
import read_file
import generateMap
import pathfinding
import copy

def calculate_path(temp_map):
    temp = copy.deepcopy(temp_map)
    tempPath, tempHist, tempSc, tempHp = pathfinding.findpath(temp)
    return (tempSc, tempPath, tempHist, tempHp)

map, state = read_file.readMap("map")
map = generateMap.randomMap(map, 0, 0)

if not state:
    map = generateMap.newMaze(map, 15, 3)
paths = [0, 0, 0, 0]

bestMap = copy.deepcopy(map)
bestScore = 0
num_threads = 8  # Sesuaikan dengan jumlah CPU core yang dimiliki (i9-11900H memiliki 8 core)

with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = []
    for _ in range(1000):
        temp = copy.deepcopy(map)
        future = executor.submit(calculate_path, temp)
        futures.append(future)

    for future in concurrent.futures.as_completed(futures):
        tempScore, tempPath, tempHist, tempHp = future.result()
        if tempScore > bestScore:
            print(tempScore)
            bestScore = tempScore
            paths = [tempPath, tempHist, tempScore, tempHp]
            bestMap = copy.deepcopy(temp)

path, history, score, health = paths
print(score)

map = pathfinding.finalMaze(bestMap, path)
history.append(map)
