import sys

def fuel_counter_upper(input_file_name):
    total = 0
    with open(input_file_name) as f:
        for line in f:
            mass = int(line)
            total += mass // 3 - 2
    
    return total

if __name__ == "__main__":
    try:
        print(fuel_counter_upper(sys.argv[1]))
    except IndexError:
        print("You forgot to provide an input file name")
