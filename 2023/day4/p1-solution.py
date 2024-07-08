def load_input():
    file = open('day4/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def get_card_numbers(card_line):
    info = card_line.split(": ")
    nums = info[1].split(" | ")
    winning = nums[0].split(" ")
    mine = nums[1].split(" ")

    winning_nums = []
    for winning_num in winning:
        if winning_num != "":
            winning_nums.append(int(winning_num))

    my_nums = []
    for my_num in mine:
        if my_num != "":
            my_nums.append(int(my_num))

    return winning_nums, my_nums


def get_num_matches(winning_nums, my_nums):
    num_matches = 0
    for my_num in my_nums:
        if my_num in winning_nums:
            num_matches += 1

    return num_matches


def get_score(winning_nums, my_nums):
    num_matches = get_num_matches(winning_nums, my_nums)
    return 0 if num_matches == 0 else 2**(num_matches - 1)


def main():
    lines = load_input()
    tot = 0
    for i, line in enumerate(lines):
        winning_nums, my_nums = get_card_numbers(line)
        card_score = get_score(winning_nums, my_nums)
        tot += card_score

    print(tot)


main()
