import sys
from intcode import Intcode
from itertools import permutations

def amplifier(program, setting=None, signal=None):
    program.run(amplifiers=[setting, signal])
    return program.output

def run_amplifiers(file_data):
    
    combinations = list(permutations(range(5)))
    maximum = 0
    winning_combo = None

    for combination in combinations:
        signal = 0
        for step in combination:
            intcode = Intcode(file_data)
            signal = amplifier(intcode, setting=step, signal=signal)
    
        if signal > maximum:
            maximum = signal
            winning_combo = combination
    print("Highest value is {} for combination {}".format(maximum, winning_combo))


if __name__ == "__main__":
    file_data = None
    with open(sys.argv[1]) as f:
        file_data = f.read()

    run_amplifiers(file_data)
