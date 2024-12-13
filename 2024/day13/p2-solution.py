A_TOKENS = 3
B_TOKENS = 1
MAX_PRESSES = 10000000
PRIZE_POSITION_OFFSET = 10000000000000


def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def parse_input(lines):
    claw_machines = []
    for i in range(0, len(lines), 4):
        a_position = lines[i][10:].split(", ")
        a_x, a_y = int(a_position[0][2:]), int(a_position[1][2:])
        b_position = lines[i + 1][10:].split(", ")
        b_x, b_y = int(b_position[0][2:]), int(b_position[1][2:])
        prize_position = lines[i + 2][7:].split(", ")
        prize_x, prize_y = int(prize_position[0][2:]) + PRIZE_POSITION_OFFSET, int(prize_position[1][2:]) + PRIZE_POSITION_OFFSET

        claw_machines.append([(a_x, a_y), (b_x, b_y), (prize_x, prize_y)])

    return claw_machines


def calculate_minimum_tokens(a_pos, b_pos, prize_pos):
    a_presses = (prize_pos[0] * b_pos[1] - prize_pos[1] * b_pos[0]) // (b_pos[1] * a_pos[0] - b_pos[0] * a_pos[1])
    b_presses = (prize_pos[0] * a_pos[1] - prize_pos[1] * a_pos[0]) // (a_pos[1] * b_pos[0] - b_pos[1] * a_pos[0])
    if a_pos[0]*a_presses + b_pos[0]*b_presses == prize_pos[0] and a_pos[1]*a_presses + b_pos[1]*b_presses == prize_pos[1]:
        return A_TOKENS * a_presses + B_TOKENS * b_presses
    else:
        return 0


def main():
    lines = load_input()
    claw_machines = parse_input(lines)

    minimum_tokens = 0
    for claw_machine in claw_machines:
        minimum_tokens += calculate_minimum_tokens(claw_machine[0], claw_machine[1], claw_machine[2])
    print(minimum_tokens)


main()
