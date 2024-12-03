import re


def load_input():
    file = open('input.txt', 'r')
    s = file.read()
    return s


def main():
    s = load_input()
    pattern = r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))'
    matches = re.findall(pattern, s)

    mul_enabled = True
    mul_instructions = []
    for match in matches:
        if match[0] == "do()":
            mul_enabled = True
        elif match[0] == "don't()":
            mul_enabled = False
        elif mul_enabled:
            mul_instructions.append(match)

    res = 0
    for match in mul_instructions:
        res += int(match[1]) * int(match[2])
    
    print(res)

main()
