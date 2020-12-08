import sys

def fuel_counter_upper(input_file_name):
    total = 0
    with open(input_file_name) as f:
        for line in f:
            mass = int(line)
            while mass:
                mass = max(0, mass // 3 - 2)
                total += mass
    
    return total

if __name__ == "__main__":
    try:
        print(fuel_counter_upper(sys.argv[1]))
    except IndexError:
        print("You forgot to provide an input file name")
