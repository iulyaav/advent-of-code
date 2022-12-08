
def main(arg: str, data: str):
    
    scores = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }

    def first_round(me: str, the_opponenent: str):
        mapper = {
            "A": "rock", 
            "B": "paper", 
            "C": "scissors",
            "X": "rock",
            "Y": "paper",
            "Z": "scissors" 
            }
        total = scores[mapper[me]]
        if mapper[the_opponenent] == mapper[me]:
            total += 3
        elif (mapper[me] == "rock" and mapper[the_opponenent] == "scissors") \
            or (mapper[me] == "scissors" and mapper[the_opponenent] == "paper") \
            or (mapper[me] == "paper" and mapper[the_opponenent] == "rock"):
            total += 6
        return total
    
    def second_round(me: str, the_opponenent: str):
        mapper = {
            "A": ["rock", "scissors", "paper"], 
            "B": ["paper", "rock", "scissors"], 
            "C": ["scissors", "paper", "rock"]}
        
        if me == "Y":  # draw
            return 3 + scores[mapper[the_opponenent][0]]
        elif me == "X":  # lose
            return scores[mapper[the_opponenent][1]]
        elif me == "Z":  # win
            return 6 + scores[mapper[the_opponenent][2]]
        

    total = 0
    for line in data.split('\n'):
        opponent, me = line.split(' ')
        if arg == "a":
            total += first_round(me, opponent)
        else:
            total += second_round(me, opponent)
    
    print(total)


