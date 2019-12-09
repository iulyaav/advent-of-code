import sys
from collections import defaultdict
from intcode import Intcode, NeedMoreInfoException
from itertools import permutations

def amplifier(program, amplifiers=None):
    program.run(amplifiers=amplifiers)
    return program.output

def run_amplifiers(file_data):
    
    combinations = list(permutations(range(5, 10)))
    maximum = 0
    winning_combo = None

    for combination in combinations:
        signal = 0
        visited = list(combination)
        amplifier_outputs = defaultdict(list)
        while visited:
            step = visited.pop(0)
            intcode = Intcode(file_data)
            try:
                if not amplifier_outputs[step]:
                    amplifier_outputs[step].append(0)
                outputs = amplifier_outputs[step]
                signal = amplifier(intcode, amplifiers=[step] + outputs)
                if visited:
                    amplifier_outputs[visited[0]].append(signal)
            except NeedMoreInfoException:
                amplifier_outputs[visited[0]].append(intcode.output)
                visited.append(step)

        if signal > maximum:
            maximum = signal
            winning_combo = combination
    print("Highest value is {} for combination {}".format(maximum, winning_combo))


if __name__ == "__main__":
    file_data = None
    with open(sys.argv[1]) as f:
        file_data = f.read()

    run_amplifiers(file_data)
