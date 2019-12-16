import sys
from intcode_paint import Intcode

def paint_robot(data):
    intcode = Intcode(data)
    intcode.run()
    whites = intcode.white_tiles

    max_x = max([x[0] for x in whites])
    min_x = min([x[0] for x in whites])
    max_y = max([x[1] for x in whites])
    min_y = min([x[1] for x in whites])

    for i in range(min_x, max_x+1):
        print("".join(["#" if (i, j) in whites else " " for j in range(min_y, max_y+1) ]))

if __name__ == "__main__":
    file_name = sys.argv[1]
    file_data = None
    with open(file_name) as f:
        file_data = f.read()
    paint_robot(file_data)