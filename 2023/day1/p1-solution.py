def load_input():
    file = open('day1/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def main():
    lines = load_input()
    tot = 0
    for i, line in enumerate(lines):
        line_nums = []
        for char in line:
            try:
                num = int(char)
                line_nums.append(num)
                break
            except:
                continue

        for char in reversed(line):
            try:
                num = int(char)
                line_nums.append(num)
                break
            except:
                continue

        tot += line_nums[0] * 10 + line_nums[1]

    print(tot)

main()
