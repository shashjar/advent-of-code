import numpy as np


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
    time_info = lines[0].split(" ")
    distance_info = lines[1].split(" ")

    times = []
    for time_elt in time_info:
        if "Time" not in time_elt and time_elt != "":
            times.append(int(time_elt))

    distances = []
    for distance_elt in distance_info:
        if "Distance" not in distance_elt and distance_elt != "":
            distances.append(int(distance_elt))

    num_ways_to_win_list = []
    for i in range(len(times)):
        num_ways_to_win = get_num_ways_to_win(times[i], distances[i])
        num_ways_to_win_list.append(num_ways_to_win)

    print(np.prod(num_ways_to_win_list))


main()
