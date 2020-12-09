def check(numbers, target):
    for i in range(25):
        for j in range(i+1, 25):
            if numbers[i] + numbers[j] == target:
                return True
    return False

def nine_a():
    with open("input_9.txt", "r") as f:
        queue = []
        cnt = 0
        line = f.readline()
        while line:
            if cnt < 25:
                queue.append(int(line))
            else:
                number = int(line)
                if check(queue, number):
                    queue.pop(0)
                    queue.append(number)
                else:
                    return number, cnt
            cnt += 1
            line = f.readline()

def find(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            if sum(numbers[i:j+1]) == target:
                return i, j

def nine_b():
    number, index = nine_a()
    queue_one = []
    queue_two = []
    cnt = 0
    with open("input_9.txt", "r") as f:
        line = f.readline()
        while line:
            if cnt < index:
                queue_one.append(int(line))
            else:
                queue_two.append(int(line))
            cnt += 1
            line = f.readline()
    
    found = find(queue_one, number)
    if found is Nont:
        found = find(queue_two, number)
    return max(queue_one[found[0]:found[1]+1]) + min(queue_one[found[0]:found[1]+1]) 
    

print(nine_b())