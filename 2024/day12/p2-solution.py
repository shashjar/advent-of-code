DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def parse_input(input):
    matrix = []
    for line in input:
        row = []
        for plant in line:
            row.append(plant)
        matrix.append(row)
    return matrix


def on_grid(pos, matrix):
    return pos[0] >= 0 and pos[0] < len(matrix) and pos[1] >= 0 and pos[1] < len(matrix[0])


def same_plant_type(r1, c1, r2, c2, matrix):
    return matrix[r1][c1] == matrix[r2][c2]


def get_neighbors(r, c, matrix):
    neighbors = []
    for direction in DIRECTIONS:
        neighbor = (r + direction[0], c + direction[1])
        if on_grid(neighbor, matrix) and same_plant_type(r, c, neighbor[0], neighbor[1], matrix):
            neighbors.append(neighbor)
    return neighbors


def dfs(r, c, visited, matrix):
    visited.add((r, c))

    region_positions = set()
    region_positions.add((r, c))

    neighbors = get_neighbors(r, c, matrix)
    for neighbor in neighbors:
        if neighbor not in visited:
            neighbor_region_positions = dfs(neighbor[0], neighbor[1], visited, matrix)
            region_positions.update(neighbor_region_positions)
    
    return region_positions


def count_corners(positions):
    num_corners = 0
    for position in positions:
        r, c = position[0], position[1]

        # Outer corners
        num_corners += (r - 1, c) not in positions and (r, c - 1) not in positions
        num_corners += (r + 1, c) not in positions and (r, c - 1) not in positions
        num_corners += (r - 1, c) not in positions and (r, c + 1) not in positions
        num_corners += (r + 1, c) not in positions and (r, c + 1) not in positions

        # Inner corners
        num_corners += (r - 1, c) in positions and (r, c - 1) in positions and (r - 1, c - 1) not in positions
        num_corners += (r + 1, c) in positions and (r, c - 1) in positions and (r + 1, c - 1) not in positions
        num_corners += (r - 1, c) in positions and (r, c + 1) in positions and (r - 1, c + 1) not in positions
        num_corners += (r + 1, c) in positions and (r, c + 1) in positions and (r + 1, c + 1) not in positions

    return num_corners


def calculate_fencing_price(matrix):
    price = 0
    visited = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if (r, c) not in visited:
                region_positions = dfs(r, c, visited, matrix)
                area = len(region_positions)
                sides = count_corners(region_positions)
                price += area * sides

    return price


def main():
    lines = load_input()
    matrix = parse_input(lines)
    price = calculate_fencing_price(matrix)
    print(price)


main()
