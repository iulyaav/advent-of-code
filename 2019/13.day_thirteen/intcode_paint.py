import sys
import time

from collections import defaultdict

class NeedMoreInfoException(Exception):
    def __init__(self):
        self.message = "Need more input values"

class NegativeAddressException(Exception):
    def __init__(self):
        self.message = "Can't access negative addresses"

class Intcode:

    def __init__(self, data):
        data_list = [int(x) for x in  data.strip().split(',')]
        self.data = defaultdict(int, list(zip(range(len(data_list)), map(int, data_list))))
        self.output = None
        self.relative_base = 0
        self.instructions = []
        self.instruction = []
        self.data[0] = 2
        self.joystick = None
        self.blocks = set()
        self.ball = None
        self.paddle = None
        self.walls = set()

    def read_instruction(self):
        if len(self.instruction) == 3:
            x, y, tile = self.instruction
            if tile == 2:
                self.blocks.add((x, y))
            elif tile == 4:
                self.ball = (x, y)
            elif tile == 3:
                self.paddle = (x, y)
            elif tile == 1:
                self.walls.add((x, y))
            elif x == -1 and y == 0 and tile not in range(5):
                self.score = tile
            else:
                self.instructions.append([x, y, tile])
            self.instruction = []

    def addition(self, index, param_1, param_2, param_3):
        self.data[param_3] = self.data[param_1] + self.data[param_2]
        return index + 4

    def multiplication(self, index, param_1, param_2, param_3):
        self.data[param_3] = self.data[param_1] * self.data[param_2]
        return index + 4

    def read(self, index, param, input_value=None):
        if input_value is None:
            if self.ball[0] > self.paddle[0]: 
                input_value = 1
            elif self.ball[0] < self.paddle[0]: 
                input_value = -1
            else: 
                input_value = 0
        self.data[param] = input_value
        return index + 2

    def write(self, index, param):
        self.output = self.data[param]
        self.instruction.append(self.output)
        self.read_instruction()
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
    
    def change_base(self, index, param_1):
        self.relative_base += self.data[param_1]
        return index + 2

    def get_parameters(self, start, steps, mode="000"):
        if steps is None:
            return

        parameter_instructions = {
                "0": lambda index: self.data[index],
                "1": lambda index: index,
                "2": lambda index: self.data[index] + self.relative_base
        }

        for i in range(steps):
            parameter = parameter_instructions[mode[-1 - i]](start+i)
            if parameter < 0:
                raise NegativeAddressException
            yield parameter

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
                9: lambda index: self.change_base(index, next(self.get_parameters(index+1, steps=1, mode=instructions))),
        }

        while True:

            opcode = self.data[index] % 10

            if opcode not in operations.keys():
                raise Exception("Oh-oh")
        
            if self.data[index] == 99:
                break

            instructions = str(self.data[index] // 100)

            if len(instructions) < 3:
                instructions = "0" * (3 - len(instructions)) + instructions
            if opcode == 3:
                amplifier = amplifiers.pop(0) if amplifiers else None
                index = operations[opcode](index, amplifier)
            else:
                index = operations[opcode](index)
            
        return

