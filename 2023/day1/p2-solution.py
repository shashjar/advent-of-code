def load_input():
    file = open('day1/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
nums_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def num_str_to_num(num_str):
    return nums_dict[num_str] if num_str in nums_dict else int(num_str)


def main():
    lines = load_input()
    tot = 0

    for i, line in enumerate(lines):
        first_ind = float("inf")
        first_digit = ""
        last_ind = -1
        last_digit = ""

        for num in nums:
            first_ind_found = line.find(num)
            last_ind_found = line.rfind(num)

            if first_ind_found != -1 and first_ind_found < first_ind:
                first_ind = first_ind_found
                first_digit = num

            if last_ind_found != -1 and last_ind_found > last_ind:
                last_ind = last_ind_found
                last_digit = num

        tot += 10 * num_str_to_num(first_digit) + num_str_to_num(last_digit)

    print(tot)

main()
