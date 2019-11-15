import random


def get_manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


'''
Return the closest coord to the target coord.

Note: If there are multiple closest coords. Then first from the order list coords will be chosen.
'''
def find_closest_coord_to_target_coord(target_coord: tuple, coords: list) -> tuple:

    closest_coord = min(coords, key=lambda coord: get_manhattan_distance(coord, target_coord))
    return closest_coord


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