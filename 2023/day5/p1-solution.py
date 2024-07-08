def load_input():
    file = open('day5/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def in_range(l, num):
    if num >= l[1] and num < l[1] + l[2]:
        return True, (num - l[1]) + l[0]
    
    return False, 0


def get_map_ranges(lines):
    map_ranges = []
    curr_range = []
    for line in lines[3:]:
        if "map" in line:  # Start of new map
            map_ranges.append(curr_range)
            curr_range = []
        elif len(line) > 0:
            curr_range.append(list(map(int, line.split(" "))))
    map_ranges.append(curr_range)

    return map_ranges


def get_seed_locs(seed_nums, map_ranges):
    seed_locs = []
    for seed_num in seed_nums:
        curr_val = seed_num
        for map_ranges_list in map_ranges:
            for map_range in map_ranges_list:
                is_in_range, new_val = in_range(map_range, curr_val)
                if is_in_range:
                    curr_val = new_val
                    break

        seed_locs.append(curr_val)

    return seed_locs


def main():
    lines = load_input()

    seed_nums = list(map(int, lines[0].split(": ")[1].split(" ")))
    map_ranges = get_map_ranges(lines)
    seed_locs = get_seed_locs(seed_nums, map_ranges)

    print(min(seed_locs))


main()
