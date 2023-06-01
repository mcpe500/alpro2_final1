import read_file
import generateMap
import pathfinding

map,state = read_file.readMap("map")
map = generateMap.randomMap(map, 0, 0)

if not state:
    map = generateMap.newMaze(map)
path,history = pathfinding.findpath(map)
map = pathfinding.finalMaze(map,path)
history.append(map)
for i in map:
    print(i)

for i in history:
    print(i)
import visualize
visualize.animate(history)


