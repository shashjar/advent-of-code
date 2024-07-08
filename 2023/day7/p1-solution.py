import functools


def load_input():
    file = open('day7/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


# Lowest individual card to highest
order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


# 1 = Five of a kind, 2 = Four of a kind, ..., 6 = One pair, 7 = High card
def get_hand_rank(hand):
    num_each_card = {}
    for card in hand:
        num_each_card[card] = 1 + num_each_card.get(card, 0)

    if len(num_each_card) == 1:
        return 1
    elif len(num_each_card) == 2 and 4 in num_each_card.values():
        return 2
    elif len(num_each_card) == 2 and 3 in num_each_card.values():
        return 3
    elif len(num_each_card) == 3 and 3 in num_each_card.values():
        return 4
    elif len(num_each_card) == 3:
        return 5
    elif len(num_each_card) == 4:
        return 6
    else:
        return 7


# 1 if hand1 is stronger, -1 if hand2 is stronger, 0 if same hand
def compare_hands(hand1_full, hand2_full):
    hand1 = hand1_full[0]
    hand2 = hand2_full[0]
    hand1_rank = get_hand_rank(hand1)
    hand2_rank = get_hand_rank(hand2)

    if hand1_rank < hand2_rank:
        return 1
    elif hand1_rank > hand2_rank:
        return -1
    else:
        for i in range(len(hand1)):
            hand1_card = hand1[i]
            hand2_card = hand2[i]

            hand1_ind = order.index(hand1_card)
            hand2_ind = order.index(hand2_card)

            if hand1_ind > hand2_ind:
                return 1
            elif hand1_ind < hand2_ind:
                return -1

        return 0


def main():
    lines = load_input()
    hands = []
    for i, line in enumerate(lines):
        info = line.split(" ")
        hand, bid = info[0], int(info[1])
        hands.append((hand, bid))

    cmp = functools.cmp_to_key(compare_hands)
    hands.sort(key=cmp)

    res = 0
    for i, hand in enumerate(hands):
        res += (i + 1) * hand[1]

    print(res)


main()
