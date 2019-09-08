import random


def get_manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def find_closest_coords_to_target_coord(target_coord: tuple, coords: list):
    manhattan_distances = [get_manhattan_distance(target_coord, c) for c in coords]

    closest_distance = min(manhattan_distances)

    indexes = []
    for i in range(len(manhattan_distances)):
        if closest_distance == manhattan_distances[i]:
            indexes.append(i)

    closest_coords = []
    for idx in indexes:
        closest_coords.append(coords[idx])
    
    return closest_coords


# Todo We can make reusable logic from this and the above methods. Similar logic
def find_furthest_coords_to_target_coord(targetCoord: tuple, coords: list):
    manhattan_distances = [get_manhattan_distance(targetCoord, c) for c in coords]

    closest_distance = max(manhattan_distances)

    indexes = []
    for i in range(len(manhattan_distances)):
        if closest_distance == manhattan_distances[i]:
            indexes.append(i)

    closest_coords = []
    for idx in indexes:
        closest_coords.append(coords[idx])
    
    return closest_coords


def find_random_position(width, height):
    x = random.randint(0, width)
    y = random.randint(0, height)
    return x, y