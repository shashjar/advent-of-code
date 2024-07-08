import numpy as np


def load_input():
    file = open('day3/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


neighbor_offsets = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]


def get_neighbor_nums(lines, start_r, start_c):
    loc_ranges_added = set()
    for offset in neighbor_offsets:
        neigh_loc = (start_r + offset[0], start_c + offset[1])
        try:
            num = int(lines[neigh_loc[0]][neigh_loc[1]])
        except:
            continue

        l = neigh_loc[1]
        r = neigh_loc[1]
        while True:
            try:
                num = int(lines[neigh_loc[0]][l - 1])
                l -= 1
            except:
                break
        while True:
            try:
                num = int(lines[neigh_loc[0]][r + 1])
                r += 1
            except:
                break

        if (neigh_loc[0], l, r) not in loc_ranges_added:
            loc_ranges_added.add((neigh_loc[0], l, r))

    neighbor_nums = []
    for loc_range in loc_ranges_added:
        num = int(lines[loc_range[0]][loc_range[1] : loc_range[2] + 1])
        neighbor_nums.append(num)

    return neighbor_nums


def is_gear(lines, r, c):
    if lines[r][c] != "*":
        return False, 0
    
    neighbor_nums = get_neighbor_nums(lines, r, c)
    return len(neighbor_nums) == 2, np.prod(neighbor_nums)


def main():
    lines = load_input()
    gear_ratio_sum = 0
    for i, line in enumerate(lines):
        for j, _ in enumerate(line):
            is_gear_pred, val = is_gear(lines, i, j)
            if is_gear_pred:
                gear_ratio_sum += val

    print(gear_ratio_sum)


main()
