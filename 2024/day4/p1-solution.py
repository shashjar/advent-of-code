import numpy as np


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def count_xmas_list(l):
    res = 0

    i = 0
    while i < len(l):
        if i + 3 < len(l) and list(l[i : i+4]) == ["X", "M", "A", "S"]:
            res += 1
            i += 4
        else:
            i += 1
    
    return res


def count_xmas(matrix):
    res = 0

    for row in matrix:
        res += count_xmas_list(row)
        res += count_xmas_list(row[::-1])
    
    for i in range(len(matrix[0])):
        col = [row[i] for row in matrix]
        res += count_xmas_list(col)
        res += count_xmas_list(col[::-1])
    
    a = np.array(matrix)
    diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
    diags.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))
    for diag in diags:
        res += count_xmas_list(diag)
        res += count_xmas_list(diag[::-1])

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
