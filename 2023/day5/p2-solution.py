def load_input():
    file = open('day5/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def in_range(l, num):
    if num >= l[0] and num < l[0] + l[2]:
        return True, (num - l[0]) + l[1]
    
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


def initial_seed(val, seed_ranges):
    for seed_range in seed_ranges:
        if val >= seed_range[0] and val < seed_range[0] + seed_range[1]:
            return True
        
    return False


def get_seed_loc(seed_ranges, reversed_map_ranges):
    seed_loc = -1
    while True:
        seed_loc += 1
        curr_val = seed_loc

        for map_ranges_list in reversed_map_ranges:
            for map_range in map_ranges_list:
                is_in_range, new_val = in_range(map_range, curr_val)
                if is_in_range:
                    curr_val = new_val
                    break

        if initial_seed(curr_val, seed_ranges):
            return seed_loc


def main():
    lines = load_input()

    seed_nums = list(map(int, lines[0].split(": ")[1].split(" ")))
    seed_ranges = []
    for i in range(0, len(seed_nums), 2):
        seed_ranges.append([seed_nums[i], seed_nums[i + 1]])

    reversed_map_ranges = get_map_ranges(lines)
    reversed_map_ranges.reverse()
    final_seed_loc = get_seed_loc(seed_ranges, reversed_map_ranges)

    print(final_seed_loc)


main()
