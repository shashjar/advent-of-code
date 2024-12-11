from collections import defaultdict


NUM_BLINKS = 75


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines[0]


def parse_input(input):
    nums = input.split(" ")
    stones = defaultdict(int)
    for num in nums:
        stones[num] += 1
    return stones


def perform_blink(stones):
    new_stones = defaultdict(int)
    for k, v in stones.items():
        if k == "0":
            new_stones["1"] += v
        elif len(k) % 2 == 0:
            midpoint = len(k) // 2
            new_stones[k[:midpoint]] += v
            new_stones[str(int(k[midpoint:]))] += v
        else:
            new_stones[str(int(k) * 2024)] += v
    return new_stones


def perform_blinks(stones, num_blinks):
    for _ in range(num_blinks):
        stones = perform_blink(stones)
    return stones


def main():
    input = load_input()
    stones = parse_input(input)
    new_stones = perform_blinks(stones, NUM_BLINKS)
    print(sum(new_stones.values()))


main()
