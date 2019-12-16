import sys
from intcode import Intcode

def paint_robot(data):
    intcode = Intcode(data)
    intcode.run()
    print(len(intcode.path))

if __name__ == "__main__":
    file_name = sys.argv[1]
    file_data = None
    with open(file_name) as f:
        file_data = f.read()
    paint_robot(file_data)