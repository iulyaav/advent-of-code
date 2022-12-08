from typing import Optional

class Folder:

    def __init__(self, name) -> None:
        self.name = name
        self.parent = None
        self.size = 0
        self.children = []
    
    def __str__(self) -> str:
        return f"Folder {self.name}, size: {self.size}: [{[str(child) for child in self.children]}]"


def parse_data(data: str) -> Folder:
    parent_folder = Folder("main")
    current_folder = None
    data = data.split('\n')
    n = len(data)
    i = 0
    while i < n:
        line = data[i]
        if line[0] == "$":
            command = line.split(' ')[1:]
            if command[0] == "cd":
                if command[1] == "/":
                    current_folder = parent_folder
                elif command[1] == "..":
                    current_folder = current_folder.parent
                else:
                    for child in current_folder.children:
                        if child.name == command[1]:
                            current_folder = child
                            break
            elif command[0] == "ls":
                i += 1
                while i < n and data[i][0] != "$":
                    ls_data = data[i].split(' ')
                    if ls_data[0] == "dir":
                        new_folder = Folder(ls_data[1])
                        new_folder.parent = current_folder
                        current_folder.children.append(new_folder)
                    else:
                        current_folder.size += int(ls_data[0])
                    i += 1
                i -= 1 
            else:
                print("Not implemented")
        i += 1
    return parent_folder



def main(arg: str, data: str):
    
    def recalculate_sizes(node: Optional[Folder]):
        if node is None:
            return 0
        extra_size = 0
        for child in node.children:
            extra_size += recalculate_sizes(child)
        node.size += extra_size
        if arg == "a" and node.size <= 100000:
            answer.append(node.size)
        else:
            answer.append(node.size) 
        return node.size
    
    answer = []
    parent_folder = parse_data(data)
    recalculate_sizes(parent_folder)
    if arg == "a":
        print(sum(answer))
    else:
        max_space = 70000000 
        space_had = max_space - parent_folder.size
        space_needed = abs(30000000 - space_had)
        answer.sort()
        left, right = 0, len(answer)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if answer[mid] > space_needed:
                right = mid - 1
            else:
                left = mid + 1
                ans = left
        print(answer[ans])


    
    
    