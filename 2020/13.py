
def thirteen_a():
    with open("input_13.txt", "r") as f:
        departure = int(f.readline().strip())
        timetable = [int(x) for x in f.readline().split(',') if x != "x"]
        res = None
        for t in timetable:
            mini = (departure // t) * t
            if mini < departure:
                mini += t
            if res is None or res[0] > (mini - departure):
                res = (mini - departure, t)
        return res[0] * res[1]    

def thirteen_b():
    with open("input_13.txt", "r") as f:
        _ = int(f.readline().strip())
        timetable = f.readline().split(',')
        step = 1
        index = 1
        while timetable:
            current = timetable.pop(0)
            if current == "x":
                step += 1
                continue
            current = int(current)



print(thirteen_a())