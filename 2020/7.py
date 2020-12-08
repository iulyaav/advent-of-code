from collections import defaultdict

def seven_a():
    target = "shiny gold"
    with open("input_7.txt", "r") as f:
        rules = defaultdict(list)
        rules_inverted = defaultdict(list)
        line = f.readline()
        while line:
            a, b = line.split("contain")
            a = a.replace(" bags ", "")
            if "no other bags" not in b:
                rlz = b.strip().split(',')
                for r in rlz:
                    bag = r.strip().split(" ")
                    bag = f"{bag[1]} {bag[2]}"
                    rules[a].append(bag)
                    rules_inverted[bag].append(a)
            line = f.readline()
        
        to_visit = rules_inverted[target]
        visited = set()
        while to_visit:
            cur = to_visit.pop()
            for p in rules_inverted[cur]:
                if p not in visited:
                    to_visit.append(p)
            visited.add(cur)
        return len(visited)
        

def seven_b():
    target = "shiny gold"
    with open("input_7.txt", "r") as f:
        rules = defaultdict(list)
        line = f.readline()
        while line:
            a, b = line.split("contain")
            a = a.replace(" bags ", "")
            if "no other bags" in b:
                rules[a] = []
                line = f.readline()
                continue
            rlz = b.strip().split(',')
            for r in rlz:
                bag = r.strip().split(" ")
                rules[a].append((bag[0], f"{bag[1]} {bag[2]}"))
            line = f.readline()
        
        return count(rules, target) - 1
        


def count(rules, target):
    if not rules[target]:
        return 1
    total = 1
    for x in rules[target]:
        cnt, name = x
        num = count(rules, name)
        total += int(cnt) * (num)
        print(f"to make 1 bag of {name} you need {num} inside bags")

    return total

 

print(seven_b())