def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def main():
    lines = load_input()
    for i, line in enumerate(lines):
        print(line)


if __name__ == "__main__":
    main()
