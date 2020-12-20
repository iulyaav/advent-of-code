class Square:
    def __init__(self, id, pixels):
        self.id = id
        self.pixels = pixels
        self.edge_up = self.pixels[0]
        self.edge_down = self.pixels[-1]
        self.edge_left = [x[0] for x in self.pixels]
        self.edge_right = [x[-1] for x in self.pixels]
        self.left = None
        self.right = None
        self.up = None
        self.down = None
    
    def check(self, square):
        if self.edge_up == square.edge_down:
            return "UP"
        elif self.edge_down == square.edge_up:
            return "DOWN"
        elif self.edge_left == square.edge_right:
            return "LEFT"
        elif self.edge_right == square.edge_left:
            return "RIGHT"
        
    def flip_vertical(self):
        self.edge_left = [x[-1] for x in self.pixels]
        self.edge_right = [x[0] for x in self.pixels]
        self.edge_up = self.pixels[0][::-1]
        self.edge_down = self.pixels[-1][::-1]
        
    def flip_horizontal(self):
        self.edge_left = [x[0] for x in self.pixels][::-1]
        self.edge_right = [x[-1] for x in self.pixels][::-1]
        self.edge_up = self.pixels[-1]
        self.edge_down = self.pixels[0]

    def flip_both(self):
        self.edge_left = [x[-1] for x in self.pixels][::-1]
        self.edge_right = [x[0] for x in self.pixels][::-1]
        self.edge_up = self.pixels[-1][::-1]
        self.edge_down = self.pixels[0][::-1]
    
    def __repr__(self):
        # return f"Square {self.id} -> U: {self.up.id if self.up else None}, D: {self.down.id if self.down else None}, L: {self.left.id if self.left else None}, R: {self.right.id if self.right else None}"
        return str(self.id)


def check_square(sq, squares):
    filled = {
        "UP": None,
        "LEFT": None,
        "RIGHT": None,
        "DOWN": None
    }
    print(sq.edge_left, sq.edge_right)
    for s2 in squares:
        if s2 != sq:
            res = sq.check(s2)
            if res:
                filled[res] = s2
    return filled

def twenty_a():
    with open("input_20.txt", "r") as f:
        data = f.read().strip().split('\n\n')
        squares = []
        for d in data:
            d = d.strip().split('\n')
            id = int(d[0].split(' ')[1][:-1])
            squares.append(Square(id, d[1:]))
        
        for s1 in squares:
            # check original
            original = check_square(s1, squares)

            # check flipped vertical
            s1.flip_vertical()
            vertical = check_square(s1, squares)
            s1.flip_vertical()

            # check flipped horizontal
            s1.flip_horizontal()
            horizontal = check_square(s1, squares)
            s1.flip_horizontal()

            # check flipped both
            s1.flip_both()
            both = check_square(s1, squares)
            s1.flip_both()

            print(s1.id)
            print(original) 
            print(vertical) 
            print(horizontal) 
            print(both)
            break
        
        # print("\n".join([str(x) for x in squares]))
        




def twenty_b():
    with open("input_20.txt", "r") as f:
        pass

print(twenty_a())