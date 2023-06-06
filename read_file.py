def readMap(name):
    import generateMap
    import json
    import numpy as np
    map = {}
    with open(f"{name}.json") as file:
        map = json.load(file)
    if map["use"]:
        return np.array(map["map"]),True
    else:
        width = int(input("Masukkan lebar map: "))
        height = int(input("Masukkan tinggi map: "))
        return generateMap.createEmptyMap(width=width,height=height),False