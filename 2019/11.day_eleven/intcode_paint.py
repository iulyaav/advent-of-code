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
        self.white_tiles = set()
        self.current_position = (0, 0)
        self.white_tiles.add(self.current_position)
        self.instructions = []
        self.direction = "UP"
        self.directions = ["UP", "RIGHT", "DOWN", "LEFT"]
        self.direction_his = []
        self.path_his = []
        self.path = set()

    def paint_and_move(self):
        if len(self.instructions) == 2:
            val, move = self.instructions
            # paint
            color = 1 if self.current_position in self.white_tiles else 0

            if color != val:
                self.path.add(self.current_position)
                if val == 1:
                    self.white_tiles.add(self.current_position)
                else:
                    self.white_tiles.remove(self.current_position)
            
                # print("Painting at {}".format(self.current_position))
            
            # change direction
            if move == 0:
                prev_direction = self.direction
                self.direction = self.directions[self.directions.index(self.direction) - 1]
                # print("Moving left from {} to {}".format(prev_direction, self.direction))
            elif move == 1:
                index = self.directions.index(self.direction) + 1
                prev_direction = self.direction
                if index == 4:
                    index = 0
                self.direction = self.directions[index]
                # print("Moving right from {} to {}".format(prev_direction, self.direction))

            # move forward
            x, y = self.current_position
            if self.direction == "UP":
                self.current_position = (x, y+1)
            elif self.direction == "RIGHT":
                self.current_position = (x+1, y)
            elif self.direction == "DOWN":
                self.current_position = (x, y-1)
            elif self.direction == "LEFT":
                self.current_position = (x - 1, y)
            self.direction_his.append(self.direction)
            self.path_his.append(self.current_position)
              
            self.instructions = []

    def addition(self, index, param_1, param_2, param_3):
        self.data[param_3] = self.data[param_1] + self.data[param_2]
        return index + 4

    def multiplication(self, index, param_1, param_2, param_3):
        self.data[param_3] = self.data[param_1] * self.data[param_2]
        return index + 4

    def read(self, index, param, input_value=None):
        if input_value is None:
            # input_value = int(input("Give me an input value: "))
            # raise NeedMoreInfoException
            if self.current_position in self.white_tiles:
                input_value = 1
            else:
                input_value = 0
        self.data[param] = input_value
        return index + 2

    def write(self, index, param):
        self.output = self.data[param]
        # print("OUTPUT at index {} with param={}: {}".format(index, param, self.output))
        self.instructions.append(self.output)
        self.paint_and_move()
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

