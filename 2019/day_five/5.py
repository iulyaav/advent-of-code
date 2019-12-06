import sys
import time

DATA = []

def addition(index, param_1, param_2, param_3):
    DATA[param_3] = DATA[param_1] + DATA[param_2]
    return index + 4

def multiplication(index, param_1, param_2, param_3):
    DATA[param_3] = DATA[param_1] * DATA[param_2]
    return index + 4

def read(index, param):
    input_value = int(input("Give me an input value: "))
    DATA[param] = input_value
    return index + 2

def write(index, param):
    print("OUTPUT at index {}: {}".format(index, DATA[param]))
    return index + 2

def get_parameters(start, steps, mode="000"):
    if steps is None:
        return

    parameter_instructions = {
            "0": lambda index: DATA[index],
            "1": lambda index: index
    }

    for i in range(steps):
        yield parameter_instructions[mode[-1 - i]](start+i)

def intcode(noun=None, verb=None):
    index = 0

    if noun is not None:
        DATA[1] = noun
    if verb is not None:
        DATA[2] = verb

    operations = {
            1: lambda index: addition(index, *get_parameters(index+1, steps=3, mode=instructions)),
            2: lambda index: multiplication(index, *get_parameters(index+1, steps=3, mode=instructions)),
            3: lambda index: read(index, next(get_parameters(index+1, steps=1, mode=instructions))),
            4: lambda index: write(index, next(get_parameters(index+1, steps=1, mode=instructions))),
    }

    while True:

        opcode = DATA[index] % 10
        instructions = str(DATA[index] // 100)

        if len(instructions) < 3:
            instructions = "0" * (3 - len(instructions)) + instructions
        try:
            index = operations[opcode](index)
        except:
            print("Something went wrong at index {} with value {}".format(index, DATA[index]))
            break

    return DATA[0]


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        DATA = [int(x) for x in f.read().split(',')]
        print(intcode())
