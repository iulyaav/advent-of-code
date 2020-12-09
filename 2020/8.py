from collections import defaultdict

def eight_a():
    program = defaultdict(list)
    accumulator = 0
    with open("input_8.txt", "r") as f:
        cnt = 0
        line = f.readline()
        while line:
            a, b = line.strip().split(" ")
            program[cnt] = {"cmd": a, "val": b}
            line = f.readline()
            cnt += 1
    index = 0
    visited = set()
    while True:
        if index in visited:
            print(f"I reached a loop, whoops -- {accumulator}")
            break
        command = program[index]
        visited.add(index)
        if command["cmd"] == "nop":
            index += 1
        elif command["cmd"] == "jmp":
            val = int(command["val"][1:])
            if command["val"][0] == "-":
                val = -val
            index += val
        elif command["cmd"] == "acc":
            val = int(command["val"][1:])
            if command["val"][0] == "-":
                val = -val
            accumulator += val
            index += 1


def switch(program, index):
    if program[index]["cmd"] == "jmp":
        program[index]["cmd"] = "nop"
    elif program[index]["cmd"] == "nop":
        program[index]["cmd"] = "jmp"
    return program


def run_program(program, m, change):
    index = 0
    accumulator = 0
    visited = set()
    program = switch(program, change)
    
    while index < m:
        if index in visited:
            program = switch(program, change)
            return
        command = program[index]
        visited.add(index)
        if command["cmd"] == "nop":
            index += 1
        elif command["cmd"] == "jmp":
            val = int(command["val"][1:])
            if command["val"][0] == "-":
                val = -val
            index += val
        elif command["cmd"] == "acc":
            val = int(command["val"][1:])
            if command["val"][0] == "-":
                val = -val
            accumulator += val
            index += 1

    program = switch(program, change)
    return accumulator

def eight_b():
    program = defaultdict(list)
    with open("input_8.txt", "r") as f:
        cnt = 0
        line = f.readline()
        while line:
            a, b = line.strip().split(" ")
            program[cnt] = {"cmd": a, "val": b}
            line = f.readline()
            cnt += 1


    to_change = [k for k, v in program.items() if v["cmd"] in ["nop", "jmp"]]
    for i in to_change:
        result = run_program(program, cnt, i)
        if result is not None:
            return result


print(eight_b())