import sys

from collections import defaultdict

def print_message(data):
    for row in data:
        print("".join(["*" if x == "0" else " " for x in row]))

def layers(data, width, height):
    layers = {}
    n = len(data)
    start = 0

    top_layer = []
    for i in range(height):
        top_layer.append([])
        for j in range(width):
            top_layer[i].append('2')

    for i in range(n // (width * height)):
        # these are layers
        for j in range(height):
            for k in range(width):
                if top_layer[j][k] == '2' and data[start+k] != '2':
                    top_layer[j][k] = data[start+k]
            start += width
        
    
    print_message(top_layer)

if __name__ == "__main__":
    file_name = sys.argv[1]
    file_data = None
    with open(file_name) as f:
        file_data = f.read()
    
    layers(file_data, width=int(sys.argv[2]), height=int(sys.argv[3]))
    