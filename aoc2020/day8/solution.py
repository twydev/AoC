with open('input.txt', 'r') as f:
    instructions = f.read().splitlines()

instruction_counters = {}
accumulator = 0

def run_instruction(current_index: int, instruction: str):
    global accumulator
    op, arg = instruction.split()
    offset = 1
    if (op == 'acc'):
        accumulator += int(arg)
    if (op == 'jmp'):
        offset = int(arg)
    # print('current', current_index, op, arg, 'accumulator', accumulator, 'offset', offset)
    return current_index + offset

def instruction_runner(instructions, termination_check):
    current_index = 0
    while True:
        if termination_check(current_index):
            return 'Loop Detected!'
        if current_index == len(instructions):
            return 'Program Completed!'
        current_instruction = instructions[current_index]
        current_index = run_instruction(current_index, current_instruction)

def instruction_has_been_visited(index):
    global instruction_counters
    visited_count = instruction_counters.get(index, 0)
    if visited_count == 0:
        instruction_counters[index] = 1
        return False
    return True

# Part1
# print(instruction_runner(instructions, instruction_has_been_visited))
# # print(instruction_counters)
# print('Accumulated value:', accumulator)

def flip_instruction(instruction: str):
    if (instruction.startswith('jmp')):
        return instruction.replace('jmp','nop')
    if (instruction.startswith('nop')):
        return instruction.replace('nop', 'jmp')

for index in range(len(instructions)):
    candidate = instructions[index]
    if candidate.startswith('acc'):
        continue
    repaired = flip_instruction(candidate)
    instructions[index] = repaired

    instruction_counters = {}
    accumulator = 0
    test_result = instruction_runner(instructions, instruction_has_been_visited)
    
    if test_result == 'Loop Detected!':
        instructions[index] = candidate
    else:
        print(test_result, 'fixed index', index, candidate, '->', repaired, 'accumulated value', accumulator)
        break

