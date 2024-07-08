def load_input():
    file = open('day6/input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def get_num_ways_to_win(time, dist):
    num_ways = 0
    for ms in range(time + 1):
        my_dist = ms * (time - ms)
        if my_dist > dist:
            num_ways += 1

    return num_ways


def main():
    lines = load_input()
    time_info = lines[0].split(": ")[1]
    time = int(time_info.replace(" ", ""))

    distance_info = lines[1].split(": ")[1]
    distance = int(distance_info.replace(" ", ""))
    
    num_ways_to_win = get_num_ways_to_win(time, distance)
    print(num_ways_to_win)


main()
