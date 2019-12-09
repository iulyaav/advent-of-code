import sys


def layers(data, width, height):
    layers = {}
    n = len(data)
    start = 0
    layers_metadata = {}

    max_layer = {
        'index': None,
        'amount': 10 ** 9
    }

    for i in range(n // (width * height)):
        layers[i] = data[start:start + width*height]
        start += width*height - 1
        layers_metadata[i] = {
            '0': layers[i].count('0'),
            '1': layers[i].count('1'),
            '2': layers[i].count('2'),
        }
        if layers_metadata[i]['0'] < max_layer['amount']:
            max_layer['amount'] = layers_metadata[i]['0']
            max_layer['index'] = i
    
    print(layers_metadata[max_layer['index']]['1'] * layers_metadata[max_layer['index']]['2'])

if __name__ == "__main__":
    file_name = sys.argv[1]
    file_data = None
    with open(file_name) as f:
        file_data = f.read()
    
    layers(file_data, width=int(sys.argv[2]), height=int(sys.argv[3]))
    