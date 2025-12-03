def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def main():
    lines = load_input()

    dial = 50
    password = 0

    for i, line in enumerate(lines):
        direction = line[0]
        num_rotations = int(line[1:])

        if direction == "L":
            dial -= num_rotations
            dial %= 100
        else:
            dial += num_rotations
            dial %= 100

        if dial == 0:
            password += 1

    print(password)


if __name__ == "__main__":
    main()
