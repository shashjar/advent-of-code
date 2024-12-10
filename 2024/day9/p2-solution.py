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


def find_free_space(memory, file_size, file_start_index):
    start_index = -1
    length = 0
    for i, file_id in enumerate(memory):
        if i >= file_start_index:
            return None

        if file_id == -1:
            if start_index == -1:
                start_index = i
            length += 1
            if length == file_size:
                return start_index
        else:
            start_index = -1
            length = 0
    
    return None


def compact_files(memory):
    file_ids = sorted(set(memory) - {-1}, reverse=True)
    for file_id in file_ids:
        file_indices = [i for i, block in enumerate(memory) if block == file_id]
        file_size = len(file_indices)

        free_space_start_index = find_free_space(memory, file_size, file_indices[0])

        if free_space_start_index is not None:
            for i in range(file_size):
                memory[free_space_start_index + i] = file_id
                memory[file_indices[i]] = -1
    
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
