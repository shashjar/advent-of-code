def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def is_m_s(matrix, r1, c1, r2, c2):
    if r1 < 0 or r1 >= len(matrix) or r2 < 0 or r2 >= len(matrix):
        return False
    if c1 < 0 or c1 >= len(matrix[0]) or c2 < 0 or c2 >= len(matrix[0]):
        return False
    
    return (matrix[r1][c1] == "M" and matrix[r2][c2] == "S") or (matrix[r1][c1] == "S" and matrix[r2][c2] == "M")


def count_xmas(matrix):
    res = 0
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if elem == "A":
                if not is_m_s(matrix, i - 1, j - 1, i + 1, j + 1):
                    continue
                elif not is_m_s(matrix, i + 1, j - 1, i - 1, j + 1):
                    continue
                else:
                    res += 1

    return res


def main():
    lines = load_input()
    matrix = []
    for _, line in enumerate(lines):
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)

    res = count_xmas(matrix)
    print(res)


main()
