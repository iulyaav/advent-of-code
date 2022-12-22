# This solves only B

def main(arg: str, data: str):
    x = 1
    cycle = 0
    text = []
    tmp = []
    data = data.split('\n')
    current_command = None
    need_to_go = 0
    val = 0
    
    while True:
        if not data:
            break

        if need_to_go == 0:
            if current_command == "addx":
                x += val
            current_command = None

        if cycle % 40 in [x-1, x, x+1]:
            tmp.append("#")
        else:
            tmp.append(" ")
        
        if len(tmp) == 40:
            text.append("".join(tmp))
            tmp = []

        if current_command is None:
            current_command = data.pop(0)
            if current_command.startswith("noop"):
                need_to_go = 1
            else:
                current_command, val = current_command.split(' ')
                val = int(val)
                need_to_go = 2
        
        cycle += 1
        need_to_go -= 1
     
    for line in text:
        print("".join(line))