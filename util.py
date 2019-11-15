import random
import math
from typing import List, Tuple
Coord = Tuple[int, int]


def get_manhattan_distance(coord1: Coord, coord2: Coord):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def get_euclidean_distance(coord1: Coord, coord2: Coord):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)


def find_closest_coord_to_target_coord(target_coord: Coord, coords: List[Coord]) -> tuple:
    return min(coords, key=lambda coord: get_euclidean_distance(coord, target_coord))


def find_furthest_coords_to_target_coord(target_coord: Coord, coords: List[Coord]):
    return max(coords, key=lambda coord: get_euclidean_distance(coord, target_coord))


def find_random_position(width: int, height: int):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    return x, y
