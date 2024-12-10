def load_input():
    file = open('input.txt', 'r')
    lines = file.read().splitlines()
    return lines


def parse_disk_space(input):
    memory = []
    curr_file_id = 0
    for i in range(0, len(input), 2):
        block_size = int(input[i])
        free_space = int(input[i + 1]) if i < len(input) - 1 else 0

        if block_size > 0:
            memory.extend([curr_file_id] * block_size)
        if free_space > 0:
            memory.extend([-1] * free_space)
        curr_file_id += 1
        
    return memory


def compact_files(memory):
    l, r = 0, len(memory) - 1
    while l < r:
        if memory[l] == -1 and memory[r] != -1:
            memory[l], memory[r] = memory[r], memory[l]
        
        while memory[l] != -1:
            l += 1
        while memory[r] == -1:
            r -= 1
                
    return memory


def calculate_checksum(memory):
    checksum = 0
    for i, file_id in enumerate(memory):
        if file_id != -1:
            checksum += i * file_id
    return checksum


def main():
    lines = load_input()
    input = lines[0]

    memory = parse_disk_space(input)
    compacted_memory = compact_files(memory)
    checksum = calculate_checksum(compacted_memory)

    print(checksum)


main()
