import read_file
import generateMap
import pathfinding
import copy

map,state = read_file.readMap("map")
result = {}
map = generateMap.randomMap(map, 0, 0)
if not state:
    map = generateMap.newMaze(map)
final_paths = None
history = []
bestScore = 0
bestScore2 = 0
while True:
    temp = copy.deepcopy(map)
    pa,hs,sc = pathfinding.findpath(temp,prevScore=bestScore)
    if sc == bestScore:
        break
    if sc is not None:
        if sc > bestScore:
            bestScore = sc
            final_paths = pa
            history = hs

# index = -1
# for i in range(len(paths)):
#     path, history, score = paths[i]
#     print(score)
#     if (score>bestScore):
#         bestScore = score
#         index = i

# path, history, score = paths[index]
print(bestScore)

# path, history, score = pathfinding.findpath(map)

map = pathfinding.finalMaze(map,final_paths)
history.append(map)
# for i in map:
#     print(i)

# for i in history:
#     print(i)
import visualize
visualize.animate(history)


