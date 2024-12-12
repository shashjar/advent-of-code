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


def get_neighbors_and_perimeter(r, c, matrix):
    neighbors, cell_perimeter = [], 0
    for direction in DIRECTIONS:
        neighbor = (r + direction[0], c + direction[1])
        if on_grid(neighbor, matrix) and same_plant_type(r, c, neighbor[0], neighbor[1], matrix):
            neighbors.append(neighbor)
        else:
            cell_perimeter += 1
    return neighbors, cell_perimeter


def dfs(r, c, visited, matrix):
    visited.add((r, c))

    total_area, total_perimeter = 1, 0

    neighbors, cell_perimeter = get_neighbors_and_perimeter(r, c, matrix)
    total_perimeter += cell_perimeter
    for neighbor in neighbors:
        if neighbor not in visited:
            neighbor_area, neighbor_perimeter = dfs(neighbor[0], neighbor[1], visited, matrix)
            total_area += neighbor_area
            total_perimeter += neighbor_perimeter
    
    return total_area, total_perimeter


def calculate_fencing_price(matrix):
    price = 0
    visited = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if (r, c) not in visited:
                area, perimeter = dfs(r, c, visited, matrix)
                price += area * perimeter

    return price


def main():
    lines = load_input()
    matrix = parse_input(lines)
    price = calculate_fencing_price(matrix)
    print(price)


main()
