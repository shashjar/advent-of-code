NUM_BLINKS = 25


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines[0]


def parse_input(input):
    stones = input.split(" ")
    for i in range(len(stones)):
        stones[i] = int(stones[i])
    return stones


def perform_blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            midpoint = len(stone_str) // 2
            new_stones.append(int(stone_str[:midpoint]))
            new_stones.append(int(stone_str[midpoint:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones


def perform_blinks(stones, num_blinks):
    for _ in range(num_blinks):
        stones = perform_blink(stones)
    return stones


def main():
    input = load_input()
    stones = parse_input(input)
    new_stones = perform_blinks(stones, NUM_BLINKS)
    print(len(new_stones))


main()
