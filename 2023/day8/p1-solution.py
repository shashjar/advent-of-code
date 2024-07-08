def load_input():
    file = open('day8/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def get_num_steps(data, instructions):
    num_steps = 0
    i = 0
    curr_elt = "AAA"
    while True:
        if curr_elt == "ZZZ":
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

    res = get_num_steps(data, instructions)
    print(res)


main()
