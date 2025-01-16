import heapq


MOVEMENT_POINTS = 1
ROTATION_POINTS = 1000
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def parse_input(lines):
    matrix, start_pos, end_pos = [], None, None
    for r, line in enumerate(lines):
        row = []
        for c, element in enumerate(line):
            row.append(element)
            if element == "S":
                start_pos = (r, c)
            elif element == "E":
                end_pos = (r, c)
        matrix.append(row)
    return matrix, start_pos, end_pos


def num_rotations(dir1, dir2):
    index_diff = abs(DIRECTIONS.index(dir1) - DIRECTIONS.index(dir2))
    return min(index_diff, 4 - index_diff)


def calculate_lowest_score(matrix, start_pos, end_pos):
    pq = []
    heapq.heappush(pq, (0, start_pos, (0, 1)))  # (score, position, direction)

    visited = set()  # Track visited states as (position, direction)

    while pq:
        curr_score, curr_pos, curr_dir = heapq.heappop(pq)

        if curr_pos == end_pos:
            return curr_score

        if (curr_pos, curr_dir) in visited:
            continue
        visited.add((curr_pos, curr_dir))

        for new_dir in DIRECTIONS:
            next_pos = (curr_pos[0] + new_dir[0], curr_pos[1] + new_dir[1])
            if matrix[next_pos[0]][next_pos[1]] not in ".E":
                continue
        
            new_score = curr_score + MOVEMENT_POINTS + ROTATION_POINTS * num_rotations(curr_dir, new_dir)
            heapq.heappush(pq, (new_score, next_pos, new_dir))
    
    return float("inf")


def main():
    lines = load_input()
    matrix, start_pos, end_pos = parse_input(lines)
    lowest_score = calculate_lowest_score(matrix, start_pos, end_pos)
    print(lowest_score)


if __name__ == "__main__":
    main()
