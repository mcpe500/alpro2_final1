def readMap(name):
    import generateMap
    import json
    map = {}
    with open(f"{name}.json") as file:
        map = json.load(file)
    if map["use"]:
        return map["map"],True
    else:
        width = int(input("Masukkan lebar map: "))
        height = int(input("Masukkan tinggi map: "))
        return generateMap.createEmptyMap(width=width,height=height),False