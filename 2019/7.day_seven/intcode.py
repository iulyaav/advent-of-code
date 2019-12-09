import sys
import time


class Intcode:

    def __init__(self, data):
        self.data = [int(x) for x in  data.strip().split(',')]
        self.output = None

    def addition(self, index, param_1, param_2, param_3):
        self.data[param_3] = self.data[param_1] + self.data[param_2]
        return index + 4

    def multiplication(self, index, param_1, param_2, param_3):
        self.data[param_3] = self.data[param_1] * self.data[param_2]
        return index + 4

    def read(self, index, param, input_value=None):
        if input_value is None:
            input_value = int(input("Give me an input value: "))
        self.data[param] = input_value
        return index + 2

    def write(self, index, param):
        self.output = self.data[param]
        # print("OUTPUT at index {}: {}".format(index, self.output))
        return index + 2

    def jump_if_true(self, index, param_1, param_2):
        if self.data[param_1] != 0:
            return self.data[param_2]
        return index + 3

    def jump_if_false(self, index, param_1, param_2):
        if self.data[param_1] == 0:
            return self.data[param_2]
        return index + 3

    def less_than(self, index, param_1, param_2, param_3):
        if self.data[param_1] < self.data[param_2]:
            self.data[param_3] = 1
        else:
            self.data[param_3] = 0
        return index + 4

    def equals(self, index, param_1, param_2, param_3):
        if self.data[param_1] == self.data[param_2]:
            self.data[param_3] = 1
        else:
            self.data[param_3] = 0
        return index + 4

    def get_parameters(self, start, steps, mode="000"):
        if steps is None:
            return

        parameter_instructions = {
                "0": lambda index: self.data[index],
                "1": lambda index: index
        }

        for i in range(steps):
            # print(self.data[parameter_instructions[mode[-1 - i]](start+i)])
            yield parameter_instructions[mode[-1 - i]](start+i)

    def run(self, noun=None, verb=None, amplifiers=None):
        index = 0

        if noun is not None:
            self.data[1] = noun
        if verb is not None:
            self.data[2] = verb

        operations = {
                1: lambda index: self.addition(index, *self.get_parameters(index+1, steps=3, mode=instructions)),
                2: lambda index: self.multiplication(index, *self.get_parameters(index+1, steps=3, mode=instructions)),
                3: lambda index, amplifier: self.read(index, next(self.get_parameters(index+1, steps=1, mode=instructions)), input_value=amplifier),
                4: lambda index: self.write(index, next(self.get_parameters(index+1, steps=1, mode=instructions))),
                5: lambda index: self.jump_if_true(index, *self.get_parameters(index+1, steps=2, mode=instructions)),
                6: lambda index: self.jump_if_false(index, *self.get_parameters(index+1, steps=2, mode=instructions)),
                7: lambda index: self.less_than(index, *self.get_parameters(index+1, steps=3, mode=instructions)),
                8: lambda index: self.equals(index, *self.get_parameters(index+1, steps=3, mode=instructions)),
        }

        while True:

            opcode = self.data[index] % 10
        
            if self.data[index] == 99:
                break

            instructions = str(self.data[index] // 100)

            if len(instructions) < 3:
                instructions = "0" * (3 - len(instructions)) + instructions
        
            try:
                if opcode == 3:
                    amplifier = amplifiers.pop(0) if amplifiers else None
                    index = operations[opcode](index, amplifier)
                else:
                    index = operations[opcode](index)
            except Exception as e:
                print("Something went wrong at index {} because: {}".format(index, e))
                break

        return

