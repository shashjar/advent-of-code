DIRECTIONS = ["up", "right", "down", "left"]


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def num_distinct_positions(matrix, start_position):
    distinct_positions = set()
    curr_direction = "up"

    curr_position = start_position
    while True:
        if curr_position[0] < 0 or curr_position[0] >= len(matrix) or curr_position[1] < 0 or curr_position[1] >= len(matrix[0]):
            return len(distinct_positions)

        distinct_positions.add(curr_position)
        if curr_direction == "up":
            next_position = (curr_position[0] - 1, curr_position[1])
        elif curr_direction == "down":
            next_position = (curr_position[0] + 1, curr_position[1])
        elif curr_direction == "left":
            next_position = (curr_position[0], curr_position[1] - 1)
        else:
            next_position = (curr_position[0], curr_position[1] + 1)

        if matrix[next_position[0]][next_position[1]] == "#":
            curr_direction = DIRECTIONS[(DIRECTIONS.index(curr_direction) + 1) % len(DIRECTIONS)]
        else:
            curr_position = next_position


def main():
    lines = load_input()
    matrix = []
    start_position = None
    for r, line in enumerate(lines):
        row = []
        for c, char in enumerate(line):
            row.append(char)
            if char == "^":
                start_position = (r, c)
        matrix.append(row)
    
    res = num_distinct_positions(matrix, start_position)
    print(res)


main()
