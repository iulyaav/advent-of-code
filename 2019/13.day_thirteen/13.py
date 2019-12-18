import sys
from intcode_paint import Intcode


if __name__ == "__main__":
    file_name = sys.argv[1]
    file_data = None
    with open(file_name) as f:
        file_data = f.read()
    
    intcode = Intcode(file_data)
    intcode.run()
    print(intcode.score)