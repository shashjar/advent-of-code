def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def parse_input(lines):
    A = int(lines[0].split(": ")[1])
    B = int(lines[1].split(": ")[1])
    C = int(lines[2].split(": ")[1])

    instructions_str = lines[4].split(": ")[1]
    instructions = list(map(int, instructions_str.split(",")))
    return {
        "A": A,
        "B": B,
        "C": C,
    }, instructions


def get_combo_operand(registers, operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    else:
        raise ValueError("Combo operand should never be 7")


def execute_instruction(registers, opcode, operand, output):
    if opcode == 0:
        operand = get_combo_operand(registers, operand)
        result = int(registers["A"] / 2**operand)
        registers["A"] = result
    elif opcode == 1:
        result = registers["B"] ^ operand
        registers["B"] = result
    elif opcode == 2:
        operand = get_combo_operand(registers, operand)
        result = operand % 8
        registers["B"] = result
    elif opcode == 3:
        pass
    elif opcode == 4:
        result = registers["B"] ^ registers["C"]
        registers["B"] = result
    elif opcode == 5:
        operand = get_combo_operand(registers, operand)
        result = operand % 8
        output.append(result)
    elif opcode == 6:
        operand = get_combo_operand(registers, operand)
        result = int(registers["A"] / 2**operand)
        registers["B"] = result
    elif opcode == 7:
        operand = get_combo_operand(registers, operand)
        result = int(registers["A"] / 2**operand)
        registers["C"] = result
    else:
        raise ValueError("Invalid opcode received:", opcode)
    
    return registers


def execute_instructions(registers, instructions):
    ip = 0
    output = []
    while ip < len(instructions):
        opcode = instructions[ip]
        operand = instructions[ip + 1]

        if opcode == 3 and registers["A"] != 0:  # Check explicitly for jump (jnz) instructions
            ip = operand
        else:
            registers = execute_instruction(registers, opcode, operand, output)
            ip += 2

    return registers, output


def main():
    lines = load_input()
    registers, instructions = parse_input(lines)

    initial_A = 1
    while True:
        registers["A"] = initial_A
        registers, output = execute_instructions(registers, instructions)
        if output == instructions:
            print("Initial Register A Value:", initial_A)
            break
        initial_A += 1


if __name__ == "__main__":
    main()
