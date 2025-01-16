import heapq
from collections import defaultdict


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


def find_best_paths(matrix, start_pos, end_pos):
    pq = []
    heapq.heappush(pq, (0, start_pos, (0, 1)))  # (score, position, direction)

    visited = set()              # Track visited states as (position, direction)
    parents = defaultdict(list)  # Map of positions to their path predecessors
    scores = {start_pos: 0}      # The smallest score encountered for each position

    while pq:
        curr_score, curr_pos, curr_dir = heapq.heappop(pq)

        if curr_pos == end_pos and curr_score > scores[end_pos]:
            continue

        if (curr_pos, curr_dir) in visited:
            continue
        visited.add((curr_pos, curr_dir))

        for new_dir in DIRECTIONS:
            next_pos = (curr_pos[0] + new_dir[0], curr_pos[1] + new_dir[1])
            if matrix[next_pos[0]][next_pos[1]] not in ".E":
                continue
        
            new_score = curr_score + MOVEMENT_POINTS + ROTATION_POINTS * num_rotations(curr_dir, new_dir)
            if next_pos not in scores or new_score < scores[next_pos]:
                scores[next_pos] = new_score
                parents[next_pos] = [curr_pos]
                heapq.heappush(pq, (new_score, next_pos, new_dir))
            elif new_score == scores[next_pos]:
                parents[next_pos].append(curr_pos)
    
    return parents, scores.get(end_pos, float("inf"))


def reconstruct_paths(parents, end_pos):
    paths_tiles = set()
    stack = [end_pos]
    while stack:
        curr_pos = stack.pop()
        if curr_pos not in parents or curr_pos in paths_tiles:
            continue

        paths_tiles.add(curr_pos)

        for parent in parents[curr_pos]:
            stack.append(parent)
    
    return paths_tiles


def main():
    lines = load_input()
    matrix, start_pos, end_pos = parse_input(lines)
    parents, lowest_score = find_best_paths(matrix, start_pos, end_pos)
    best_paths_tiles = reconstruct_paths(parents, end_pos)
    print("Lowest Score:", lowest_score)
    print("Number of Tiles in Best Paths:", len(best_paths_tiles))


if __name__ == "__main__":
    main()
