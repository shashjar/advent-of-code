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

        for click in range(1, num_rotations + 1):
            if direction == "L":
                new_dial = (dial - click) % 100
            else:
                new_dial = (dial + click) % 100
            
            if new_dial == 0:
                password += 1
        
        if direction == "L":
            dial = (dial - num_rotations) % 100
        else:
            dial = (dial + num_rotations) % 100

    print(password)


if __name__ == "__main__":
    main()
