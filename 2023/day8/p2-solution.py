from math import gcd # Python versions 3.5 and above
from functools import reduce # Python version 3.x


def lcm(denominators):
    return reduce(lambda a, b: a*b // gcd(a, b), denominators)


def load_input():
    file = open('day8/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def all_end_in_z(elts):
    for elt in elts:
        if elt[-1] != "Z":
            return False
        
    return True


def get_new_elts(data, elts, ind):
    new_elts = []
    for elt in elts:
        new_elt = data[elt][ind]
        new_elts.append(new_elt)

    return new_elts

def get_num_steps(data, instructions, start_elt):
    num_steps = 0
    i = 0
    curr_elt = start_elt
    while True:
        if curr_elt[-1] == "Z":
            return num_steps

        ind = i % len(instructions)
        instruction = instructions[ind]

        num_steps += 1
        if instruction == "L":
            curr_elt = data[curr_elt][0]
        else:
            curr_elt = data[curr_elt][1]

        i += 1


def main():
    lines = load_input()
    instructions = lines[0]
    lines = lines[2:]

    data = {}
    for i, line in enumerate(lines):
        info = line.split(" = ")
        elt = info[0]

        dir_info = info[1][1:-1]
        l, r = dir_info.split(", ")

        data[elt] = (l, r)

    nums = []
    for elt in data:
        if elt[-1] == "A":
            num_steps = get_num_steps(data, instructions, elt)
            nums.append(num_steps)

    print(lcm(nums))


main()
