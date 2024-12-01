def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def main():
    lines = load_input()
    left, right = [], []
    for _, line in enumerate(lines):
        nums = line.split(" ")
        left_num = int(nums[0])
        right_num = int(nums[-1])

        left.append(left_num)
        right.append(right_num)

    res = 0 
    for num in left:
        res += num * right.count(num)

    print(res)


main()
