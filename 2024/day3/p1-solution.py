import re


def load_input():
    file = open('input.txt', 'r')
    s = file.read()
    return s


def main():
    s = load_input()
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, s)

    res = 0
    for match in matches:
        res += int(match[0]) * int(match[1])
    
    print(res)


main()
