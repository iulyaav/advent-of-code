from typing import List

def main(arg: str, data: str):
    def get_index(letter: str):
        if letter.islower():
            return ord(letter) - 96
        return ord(letter) - 38
    
    def find_common(elves: List):
        commons = [False] * 53
        for letter in elves[0]:
            index = get_index(letter)
            commons[index] = True
        for i in range(1, len(elves)):
            elf = elves[i]
            tmp_commons = [False] * 53
            for j in range(len(elf)):
                index = get_index(elf[j])
                tmp_commons[index] = True
            for j in range(53):
                commons[j] = commons[j] and tmp_commons[j]
        
        priorities = 0
        for i in range(53):
            if commons[i]:
                priorities += i
        return priorities

    result = 0
    groups = []
    for line in data.split('\n'):
        if arg in ["a"]:
            middle = len(line) // 2
            groups += [line[:middle], line[middle:]]
        else:
            groups.append(line)
    
    step = 2 if arg in ["a"] else 3

    for i in range(0, len(groups), step):
        tmp_group = []
        for j in range(step):
            if i + j < len(groups):
                tmp_group.append(groups[i+j])
        result += find_common(tmp_group)

    print(result)
