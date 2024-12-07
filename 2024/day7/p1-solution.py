def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def equation_possibly_true(nums, test_value):
    if len(nums) == 1:
        return nums[0] == test_value
    
    add = equation_possibly_true([nums[0] + nums[1]] + nums[2:], test_value)
    mul = equation_possibly_true([nums[0] * nums[1]] + nums[2:], test_value)
    return add or mul


def main():
    lines = load_input()
    res = 0
    for i, line in enumerate(lines):
        parts = line.split(":")
        test_value = int(parts[0])
        nums = list(map(lambda x: int(x), parts[1].split(" ")[1:]))
        if equation_possibly_true(nums, test_value):
            res += test_value
        
    print(res)


main()
