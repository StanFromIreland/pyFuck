# PyFuck is a simple BrainFuck interpreter and compiler written in Python
import fire

def get_input(filename):
    global file_path
    file_path = str(filename)

fire.Fire(get_input)

file = open(file_path, "r")
program = list(str(file.read()))

tape = [0]
current_cell_index = 0
current_instruction = 0

user_input = []
loop_table = {}

loop_stack = []
for k, instruction in enumerate(program):
    if instruction == "[":
        loop_stack.append(k)
    elif instruction == "]":
        loop_beginning_index = loop_stack.pop()
        loop_table[loop_beginning_index] = k
        loop_table[k] = loop_beginning_index



while current_instruction < len(program):
    instruction = program[current_instruction]

    if instruction == "+":
        tape[current_cell_index] += 1
        if tape[current_cell_index] == 256:
            tape[current_cell_index] = 0
    elif instruction == "-":
        tape[current_cell_index] -= 1
        if tape[current_cell_index] == -1:
            tape[current_cell_index] = 255
    elif instruction == "<":
        current_cell_index -= 1
    elif instruction == ">":
        current_cell_index += 1
        if current_cell_index == len(tape):
            tape.append(0)
    elif instruction == ".":
        print(chr(tape[current_cell_index]), end="")
    elif instruction == ",":
        if not user_input:
            user_input = list(input() + "\n")
        tape[current_cell_index] = ord(user_input.pop(0))
    elif instruction == "[":
        if not tape[current_cell_index]:
            current_instruction = loop_table[current_instruction]
    elif instruction == "]":
        if tape[current_cell_index]:
            current_instruction = loop_table[current_instruction]

    current_instruction += 1