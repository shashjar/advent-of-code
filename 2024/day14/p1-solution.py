import math


WIDTH = 101
HEIGHT = 103
NUM_SECONDS = 100


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def parse_input(lines):
    robots = []
    for line in lines:
        parts = line.split(" ")
        position = list(map(lambda x: int(x), parts[0][2:].split(",")))
        velocity = list(map(lambda x: int(x), parts[1][2:].split(",")))
        robots.append([position, velocity])
    return robots


def simulate_step(robots):
    new_robots = []
    for robot in robots:
        new_x, new_y = (robot[0][0] + robot[1][0]) % WIDTH, (robot[0][1] + robot[1][1]) % HEIGHT
        new_robots.append([[new_x, new_y], robot[1]])
    return new_robots


def simulate_time(robots, num_seconds):
    for _ in range(num_seconds):
        robots = simulate_step(robots)
    return robots


def get_quadrant(x, y):
    midpoint_x, midpoint_y = WIDTH // 2, HEIGHT // 2
    if x > midpoint_x and y < midpoint_y:
        return 1
    elif x < midpoint_x and y < midpoint_y:
        return 2
    elif x < midpoint_x and y > midpoint_y:
        return 3
    elif x > midpoint_x and y > midpoint_y:
        return 4
    else:
        return None


def calculate_safety_factor(robots):
    num_robots_by_quadrant = {}
    for robot in robots:
        quadrant = get_quadrant(robot[0][0], robot[0][1])
        if quadrant is not None:
            num_robots_by_quadrant[quadrant] = 1 + num_robots_by_quadrant.get(quadrant, 0)
    return math.prod(num_robots_by_quadrant.values())


def main():
    lines = load_input()
    robots = parse_input(lines)
    robots = simulate_time(robots, NUM_SECONDS)
    safety_factor = calculate_safety_factor(robots)
    print(safety_factor)


if __name__ == "__main__":
    main()
