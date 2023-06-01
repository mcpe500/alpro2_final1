import read_file
import generateMap
import pathfinding

map = read_file.readMap("map")
map = generateMap.randomMap(map, 0, 0)
map = generateMap.newMaze(map)
path = pathfinding.findpath(map)
map = pathfinding.finalMaze(map,path)
for i in map:
    print(i)
import visualize
visualize.drawMaze(map,5)


