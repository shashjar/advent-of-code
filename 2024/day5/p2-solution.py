def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines

# rules[i] = j --> i has to come before j
def correctly_ordered(nums, rules):
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] in rules[nums[i]]:
                before, after = nums[i], nums[j]
                nums[j] = before
                nums[i] = after
                new_nums, _ = correctly_ordered(nums, rules)
                return new_nums, False
    
    return nums, True


def main():
    lines = load_input()
    collecting_rules = True
    rules = {}
    res = 0
    for i, line in enumerate(lines):
        if line == "":
            collecting_rules = False
            continue
        elif collecting_rules:
            parts = line.split("|")
            if parts[0] in rules:
                rules[parts[0]].add(parts[1])
            else:
                rules[parts[0]] = set([parts[1]])
        else:
            parts = line.split(",")
            new_order, originally_correct = correctly_ordered(parts, rules)
            if not originally_correct:
                res += int(new_order[len(new_order) // 2])
    
    print(res)


main()
