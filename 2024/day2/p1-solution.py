def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def safe_report(report):
    if report[1] > report[0]:
        increasing = True
    else:
        increasing = False

    for i in range(1, len(report)):
        if increasing and report[i] - report[i - 1] >= 1 and report[i] - report[i - 1] <= 3:
            continue
        elif not increasing and report[i - 1] - report[i] >= 1 and report[i - 1] - report[i] <= 3:
            continue
        else:
            return False
        
    return True


def main():
    lines = load_input()
    reports = []
    for i, line in enumerate(lines):
        nums = line.split(" ")
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        reports.append(nums)
    
    res = 0
    for report in reports:
        if safe_report(report):
            res += 1

    print(res)


main()
