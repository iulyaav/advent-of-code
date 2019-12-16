import sys
from intcode import Intcode, NeedMoreInfoException

def boost(data):
    intcode = Intcode(data)
    intcode.run(amplifiers=[2])



if __name__ == "__main__":
    file_data = None
    with open(sys.argv[1]) as f:
        file_data = f.read()

    boost(file_data)