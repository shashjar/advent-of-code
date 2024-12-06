DIRECTIONS = ["up", "right", "down", "left"]


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def stuck_in_loop(matrix, start_position, new_obstruction):
    states = set()
    curr_state = (start_position[0], start_position[1], "up")

    while True:
        if curr_state[0] < 0 or curr_state[0] >= len(matrix) or curr_state[1] < 0 or curr_state[1] >= len(matrix[0]):
            return False

        if curr_state in states:
            return True

        states.add(curr_state)
        if curr_state[2] == "up":
            next_position = (curr_state[0] - 1, curr_state[1])
        elif curr_state[2] == "down":
            next_position = (curr_state[0] + 1, curr_state[1])
        elif curr_state[2] == "left":
            next_position = (curr_state[0], curr_state[1] - 1)
        else:
            next_position = (curr_state[0], curr_state[1] + 1)

        if next_position[0] < 0 or next_position[0] >= len(matrix) or next_position[1] < 0 or next_position[1] >= len(matrix[0]):
            return False

        if matrix[next_position[0]][next_position[1]] == "#" or next_position == new_obstruction:
            new_direction = DIRECTIONS[(DIRECTIONS.index(curr_state[2]) + 1) % len(DIRECTIONS)]
            curr_state = (curr_state[0], curr_state[1], new_direction)
        else:
            curr_state = (next_position[0], next_position[1], curr_state[2])


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
    
    res = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == ".":
                if stuck_in_loop(matrix, start_position, (r, c)):
                    res += 1

    print(res)


main()
