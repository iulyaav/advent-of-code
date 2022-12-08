
def main(arg: str, data: str):
    n = len(data)
    look_for = 4 if arg == "a" else 14
    for i in range(n-look_for):
        chars = set()
        for j in range(look_for):
            chars.add(data[i+j])
        if len(chars) == look_for:
            print(i+look_for)
            break