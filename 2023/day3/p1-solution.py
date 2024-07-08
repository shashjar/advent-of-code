def load_input():
    file = open('day3/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


neighbor_offsets = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

def get_adj_num_locs(lines, part_locations):
    num_locs = set()
    for part_loc in part_locations:
        for offset in neighbor_offsets:
            neigh_loc = (part_loc[0] + offset[0], part_loc[1] + offset[1])
            try:
                num = int(lines[neigh_loc[0]][neigh_loc[1]])
                num_locs.add(neigh_loc)
            except:
                continue

    return num_locs


def get_part_number_sum(lines, num_locs):
    part_number_sum = 0
    loc_ranges_added = set()
    for num_loc in num_locs:
        l = num_loc[1]
        r = num_loc[1]
        while True:
            try:
                num = int(lines[num_loc[0]][l - 1])
                l -= 1
            except:
                break
        while True:
            try:
                num = int(lines[num_loc[0]][r + 1])
                r += 1
            except:
                break

        if (num_loc[0], l, r) not in loc_ranges_added:
            part_number = int(lines[num_loc[0]][l : r + 1])
            part_number_sum += part_number
            loc_ranges_added.add((num_loc[0], l, r))

    return part_number_sum


def main():
    lines = load_input()
    part_locations = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            try:
                _ = int(char)
            except:
                if char != ".":
                    part_locations.append((i, j))

    num_locs = get_adj_num_locs(lines, part_locations)
    part_number_sum = get_part_number_sum(lines, num_locs)
    print(part_number_sum)


main()
