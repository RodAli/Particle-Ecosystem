def getManhattanDistance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def findClosestCoordsToTargetCoord(targetCoord: tuple, coords: tuple):
    manhattanDistances = [getManhattanDistance(targetCoord, c) for c in coords]

    closestDistance = min(manhattanDistances)

    indexes = []
    for i in range(len(manhattanDistances)):
        if closestDistance == manhattanDistances[i]:
            indexes.append(i)

    closestCoords = []
    for idx in indexes:
        closestCoords.append(coords[idx])
    
    return closestCoords