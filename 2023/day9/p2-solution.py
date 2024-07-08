def load_input():
    file = open('day9/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def all_zeroes(seq):
    for num in seq:
        if num != 0:
            return False
        
    return True


def get_next_history_value(seq):
    if all_zeroes(seq):
        return 0
    
    sub_seq = []
    for i in range(1, len(seq)):
        diff = seq[i] - seq[i - 1]
        sub_seq.append(diff)

    return seq[-1] + get_next_history_value(sub_seq)


def main():
    lines = load_input()
    sequences = []
    for i, line in enumerate(lines):
        info = list(map(int, line.split(" ")))
        sequences.append(info)

    res = 0
    for seq in sequences:
        seq.reverse()
        next_history_val = get_next_history_value(seq)
        res += next_history_val

    print(res)

main()
