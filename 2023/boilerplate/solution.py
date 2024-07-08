def load_input():
    file = open('day1/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def main():
    lines = load_input()
    for i, line in enumerate(lines):
        print(line)


main()
