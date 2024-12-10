DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def parse_input():
    map = []
    lines = load_input()
    for line in lines:
        row = []
        for element in line:
            row.append(int(element))
        map.append(row)
    return map


def on_map(position, map):
    return position[0] >= 0 and position[0] < len(map) and position[1] >= 0 and position[1] < len(map[0])


def dfs(curr_r, curr_c, visited, map):
    reachable_9_positions = set()

    if map[curr_r][curr_c] == 9:
        reachable_9_positions.add((curr_r, curr_c))
        return reachable_9_positions

    visited.add((curr_r, curr_c))

    for direction in DIRECTIONS:
        neighbor_position = (curr_r + direction[0], curr_c + direction[1])
        if on_map(neighbor_position, map) and map[neighbor_position[0]][neighbor_position[1]] == map[curr_r][curr_c] + 1 and neighbor_position not in visited:
            reachable_9_positions.update(dfs(neighbor_position[0], neighbor_position[1], visited, map))
    
    visited.remove((curr_r, curr_c))

    return reachable_9_positions


def calculate_trailhead_score_sum(map):
    trailhead_score_sum = 0
    for r, row in enumerate(map):
        for c, height in enumerate(row):
            if height == 0:
                reachable_9_positions = dfs(r, c, set(), map)
                trailhead_score_sum += len(reachable_9_positions)
    return trailhead_score_sum


def main():
    map = parse_input()
    trailhead_score_sum = calculate_trailhead_score_sum(map)
    print(trailhead_score_sum)


main()
