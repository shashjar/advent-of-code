def load_input():
    file = open('day4/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def get_card_numbers(card_line):
    info = card_line.split(": ")
    card_num = int(info[0].split(" ")[-1])
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

    return card_num, winning_nums, my_nums


def get_num_matches(winning_nums, my_nums):
    num_matches = 0
    for my_num in my_nums:
        if my_num in winning_nums:
            num_matches += 1

    return num_matches


def main():
    lines = load_input()
    num_cards = {}
    for i, line in enumerate(lines):
        card_num, winning_nums, my_nums = get_card_numbers(line)
        num_cards[card_num] = 1 + num_cards.get(card_num, 0)
        num_matches = get_num_matches(winning_nums, my_nums)
        
        num_new_copies = num_cards[card_num]
        start_card, end_card = card_num + 1, card_num + num_matches
        for dup_card in range(start_card, end_card + 1):
            num_cards[dup_card] = num_new_copies + num_cards.get(dup_card, 0)

    print(sum(num_cards.values()))


main()
