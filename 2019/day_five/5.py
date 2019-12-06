import sys
import time

def intcode(data, noun=None, verb=None):
    index = 0

    if noun is not None:
        data[1] = noun
    if verb is not None:
        data[2] = verb
    while data[index] % 100 != 99:

        opcode = data[index] % 10
        instructions = str(data[index] // 100)

        if len(instructions) < 3:
            instructions = "0" * (3 - len(instructions)) + instructions

        if opcode == 1:
            param_1 = data[data[index + 1]] if instructions[2] == "0" else data[index + 1]
            param_2 = data[data[index + 2]] if instructions[1] == "0" else data[index + 2]
            param_3 = data[index + 3] if instructions[0] == "0" else index + 3

            data[param_3] = param_1 + param_2
            index += 4

        elif opcode == 2:
            param_1 = data[data[index + 1]] if instructions[2] == "0" else data[index + 1]
            param_2 = data[data[index + 2]] if instructions[1] == "0" else data[index + 2]
            param_3 = data[index + 3] if instructions[0] == "0" else index + 3
            
            data[param_3] = param_1 * param_2
            index += 4

        elif opcode == 3:
            print("Gimme value")
            input_value = int(input())
            param = data[index+1] if instructions[2] == "0" else index+1
            data[param] = input_value
            index += 2

        elif opcode == 4:
            param = data[index+1] if instructions[2] == "0" else index+1
            print("OUTPUT at index {}: {}".format(index, data[param]))
            index += 2
        
        else:
            print("Something went wrong at index {} with value {}".format(index, data[index]))
            break

    return data[0]


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = [int(x) for x in f.read().split(',')]
        print(intcode(data))
