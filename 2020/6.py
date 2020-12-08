
def six_a():
    with open("input_6.txt", "r") as f:
        groups = f.read().split('\n\n')
        res = 0
        for group in groups:
            people = group.split('\n')
            dif_questions = set()
            for p in people:
                dif_questions = dif_questions.union(set(list(p)))
            res += len(dif_questions)
        return res


def six_b():
    with open("input_6.txt", "r") as f:
        groups = f.read().split('\n\n')
        res = 0
        for group in groups:
            people = group.split('\n')
            dif_questions = set(list("qwertyuiopasdfghjklzxcvbnm"))
            for p in people:
                dif_questions = dif_questions.intersection(set(list(p)))
            res += len(dif_questions)
        return res
 

print(six_a())