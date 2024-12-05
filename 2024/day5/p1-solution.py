def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines

# rules[i] = j --> i has to come before j
def correctly_ordered(nums, rules):
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] in rules[nums[i]]:
                return False
    
    return True


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
            if correctly_ordered(parts, rules):
                res += int(parts[len(parts) // 2])
    
    print(res)


main()
