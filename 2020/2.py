
def two_a():
    with open("input_2.txt", "r") as f:
        counter = 0
        line = f.readline()

        while line:
            limits, letter, password = line.split(' ')
            limit_min, limit_max = [int(x) for x in limits.split('-')]
            letter = letter[:-1]
            cnt = 0
            for l in password:
                if l == letter:
                    cnt += 1
            if limit_min <= cnt and cnt <= limit_max:
                counter += 1
            line = f.readline()
        
        return counter


def two_b():
    with open("input_2.txt", "r") as f:
        counter = 0
        line = f.readline()

        while line:
            limits, letter, password = line.split(' ')
            limit_min, limit_max = [int(x) for x in limits.split('-')]
            letter = letter[:-1]
            if password[limit_min-1] == letter and password[limit_max-1] == letter:
                pass
            elif password[limit_min-1] == letter or password[limit_max-1] == letter:
                counter += 1
            line = f.readline()
        
        return counter

print(two_b())