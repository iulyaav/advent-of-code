import sys
import collections

def not_more_than_two(number):
    return 2 in collections.Counter(number).values()

def has_double_digits(number):
    for v in collections.Counter(number).values():
        if v >= 2:
            return True
    return False

def find_number(start, out, n, numbers=None):
    # print("{} -> {}".format(start, out))
    if numbers is None:
        numbers = []

    if n == 0:
        first_digit = out[0]
        if not_more_than_two(out):
            numbers.append(int(out))
        return
    
    for i in range(start, 10):
        str1 = out + str(i)
        find_number(i, str1, n-1, numbers)
    
    return numbers

def secure_container(data):
    lower, upper = [int(x) for x in data.split('-')]
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    total = 0
    res = [x for x in find_number(lower // 100000, "", 6) if x >= lower and x <= upper]
    return len(res)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(secure_container(f.read()))
