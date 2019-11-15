import random
from typing import List, Tuple
Coord = Tuple[int, int]


def get_manhattan_distance(coord1: Coord, coord2: Coord):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def find_closest_coord_to_target_coord(target_coord: Coord, coords: List[Coord]) -> tuple:
    return min(coords, key=lambda coord: get_manhattan_distance(coord, target_coord))


def find_furthest_coords_to_target_coord(target_coord: Coord, coords: List[Coord]):
    return max(coords, key=lambda coord: get_manhattan_distance(coord, target_coord))


def find_random_position(width: int, height: int):
    x = random.randint(0, width)
    y = random.randint(0, height)
    return x, y
