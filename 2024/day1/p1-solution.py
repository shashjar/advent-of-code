def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def main():
    lines = load_input()
    left, right = [], []
    for _, line in enumerate(lines):
        nums = line.split(" ")
        left_num, right_num = int(nums[0]), int(nums[-1])
        left.append(left_num)
        right.append(right_num)

    left.sort()
    right.sort()

    res = 0 
    for num1, num2 in zip(left, right):
        res += abs(num2 - num1)

    print(res)


main()
