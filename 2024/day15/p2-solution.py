MOVES = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def parse_input(lines):
    map, robot_pos, moves = [], None, []
    building_map = True
    for r, line in enumerate(lines):
        if line == "":
            building_map = False
            continue

        if building_map:
            row = []
            for c, element in enumerate(line):
                if element == "@":
                    row += ["@", "."]
                    robot_pos = (r, c)
                elif element == "O":
                    row += ["[", "]"]
                else:
                    row += [element, element]
            map.append(row)
        else:
            for move in line:
                moves.append(move)
    
    return map, robot_pos, moves


# TODO: needs to be modified to account for vertical movement of boxes
def push_boxes(map, robot_pos, curr_pos, direction):
    empty_pos = None
    while True:
        if map[curr_pos[0]][curr_pos[1]] == "#":
            return map, robot_pos
        elif map[curr_pos[0]][curr_pos[1]] == ".":
            empty_pos = curr_pos
            break
        else:
            curr_pos = (curr_pos[0] + direction[0], curr_pos[1] + direction[1])
    
    replacement_pos = empty_pos
    while True:
        from_pos = (replacement_pos[0] - direction[0], replacement_pos[1] - direction[1])
        map[replacement_pos[0]][replacement_pos[1]] = map[from_pos[0]][from_pos[1]]
        replacement_pos = from_pos
        if from_pos == robot_pos:
            map[robot_pos[0]][robot_pos[1]] = "."
            break

    return map, (robot_pos[0] + direction[0], robot_pos[1] + direction[1])


def simulate_move(map, robot_pos, move):
    direction = MOVES[move]
    new_robot_pos = (robot_pos[0] + direction[0], robot_pos[1] + direction[1])
    if map[new_robot_pos[0]][new_robot_pos[1]] == ".":
        map[new_robot_pos[0]][new_robot_pos[1]] = "@"
        map[robot_pos[0]][robot_pos[1]] = "."
        return map, new_robot_pos
    elif map[new_robot_pos[0]][new_robot_pos[1]] == "#":
        return map, robot_pos
    else:
        return push_boxes(map, robot_pos, new_robot_pos, direction)


def simulate_moves(map, robot_pos, moves):
    for move in moves:
        map, robot_pos = simulate_move(map, robot_pos, move)
    return map, robot_pos


def calculate_gps_coordinate_sum(map):
    gps_coordinate_sum = 0
    for r, row in enumerate(map):
        for c, element in enumerate(row):
            if element == "[":
                gps_coordinate_sum += 100 * r + c
    return gps_coordinate_sum


def main():
    lines = load_input()
    map, robot_pos, moves = parse_input(lines)
    map, robot_pos = simulate_moves(map, robot_pos, moves)
    gps_coordinate_sum = calculate_gps_coordinate_sum(map)
    print(gps_coordinate_sum)


if __name__ == "__main__":
    main()
