import numpy as np

def load_input():
    file = open('day2/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


INITIAL_BAG = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def get_cube_set_map(cube_set):
    cube_set_map = {}
    cube_types = cube_set.strip().split(", ")
    for cube_type in cube_types:
        cube_info = cube_type.split(" ")
        cube_set_map[cube_info[1]] = int(cube_info[0]) + cube_set_map.get(cube_info[1], 0)

    return cube_set_map


def get_min_initial_bag(game_cube_set_maps):
    min_initial_bag = {}
    for color in ["red", "green", "blue"]:
        min_initial_bag[color] = 0

    for set_map in game_cube_set_maps:
        for color in set_map:
            min_initial_bag[color] = max(min_initial_bag[color], set_map[color])

    return min_initial_bag


def main():
    power_sum = 0

    lines = load_input()
    for i, line in enumerate(lines):
        _, cubes_revealed = line.split(": ")
        cube_sets = cubes_revealed.split(";")
        game_cube_set_maps = []
        for cube_set in cube_sets:
            cube_set_map = get_cube_set_map(cube_set)
            game_cube_set_maps.append(cube_set_map)

        min_initial_bag = get_min_initial_bag(game_cube_set_maps)
        power_sum += np.prod(list(min_initial_bag.values()))

    print(power_sum)

main()
