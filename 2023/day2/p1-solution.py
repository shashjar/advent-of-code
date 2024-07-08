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


def valid_game(game_cube_set_maps, initial_bag):
    for set_map in game_cube_set_maps:
        for color in set_map:
            if set_map[color] > initial_bag[color]:
                return False
            
    return True


def main():
    game_id_sum = 0

    lines = load_input()
    for i, line in enumerate(lines):
        game_info, cubes_revealed = line.split(": ")
        game_id = int(game_info.split(" ")[1])
        cube_sets = cubes_revealed.split(";")
        game_cube_set_maps = []
        for cube_set in cube_sets:
            cube_set_map = get_cube_set_map(cube_set)
            game_cube_set_maps.append(cube_set_map)

        if valid_game(game_cube_set_maps, INITIAL_BAG):
            game_id_sum += game_id

    print(game_id_sum)

main()
