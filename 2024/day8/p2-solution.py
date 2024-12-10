from collections import defaultdict


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def on_grid(pos, matrix):
    return pos[0] >= 0 and pos[0] < len(matrix) and pos[1] >= 0 and pos[1] < len(matrix[0])


def calculate_antinode_positions(matrix, pos1, pos2):
    antinode_positions = []

    row_diff, col_diff = pos2[0] - pos1[0], pos2[1] - pos1[1]
    
    i = 0
    while True:
        antinode_pos1 = (pos2[0] + i * row_diff, pos2[1] + i * col_diff)
        on_grid1 = on_grid(antinode_pos1, matrix)
        if on_grid1:
            antinode_positions.append(antinode_pos1)

        antinode_pos2 = (pos1[0] - i * row_diff, pos1[1] - i * col_diff)
        on_grid2 = on_grid(antinode_pos2, matrix)
        if on_grid2:
            antinode_positions.append(antinode_pos2)
        
        if not on_grid1 and not on_grid2:
            break

        i += 1

    return antinode_positions


def calculate_frequency_unique_antinode_locations(matrix, positions):
    unique_antinode_locations = set()

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            pos1, pos2 = positions[i], positions[j]
            antinode_positions = calculate_antinode_positions(matrix, pos1, pos2)
            unique_antinode_locations.update(antinode_positions)
        
    return unique_antinode_locations


def num_unique_antinode_locations(matrix, antenna_positions):
    unique_antinode_locations = set()

    for frequency in antenna_positions:
        frequency_unique_antinode_locations = calculate_frequency_unique_antinode_locations(matrix, antenna_positions[frequency])
        unique_antinode_locations.update(frequency_unique_antinode_locations)

    return len(unique_antinode_locations)


def main():
    matrix = []

    antenna_positions = defaultdict(list)

    lines = load_input()
    for r, line in enumerate(lines):
        row = []
        for c, char in enumerate(line):
            row.append(char)

            if char != ".":
                antenna_positions[char].append((r, c))
        matrix.append(row)
    
    res = num_unique_antinode_locations(matrix, antenna_positions)
    print(res)


main()
