import sys

class Moon:

    def __init__(self, pos):
        self.pos = pos
        self.velocity = [0, 0, 0]
    
    def increase_velocity(self, pos):
        self.velocity[pos] += 1
    
    def decrease_velocity(self, pos):
        self.velocity[pos] -= 1
    
    def apply_velocity(self):
        for i in range(3):
            self.pos[i] += self.velocity[i]
    
    def print(self):
        print("<x={}, y={}, z={}> --- <x={}, y={}, z={}>".format(self.pos[0], self.pos[1], self.pos[2], *self.velocity))

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def step(A, B):
    for i in range(3):
        if A.pos[i] < B.pos[i]:
            A.increase_velocity(i)
            B.decrease_velocity(i)
        elif A.pos[i] > B.pos[i]:
            A.decrease_velocity(i)
            B.increase_velocity(i)

def matches_initial_state(initial_values, values, pos, size):
    for i in range(size):
        if initial_values[i][pos] != values[i][pos] or initial_values[i][pos+3] != values[i][pos+3]:
            return False
    return True

def stop_cycles(cycles):
    for c in cycles:
        if c is None:
            return False
    return True

def apply_steps(moons):
    m = len(moons)
    counter = 1
    initial_values = [[*i.pos, *i.velocity] for i in moons]
    cycles = [None, None, None]
    while True:
        for j in range(m):
            moon = moons[j]
            for k in range(j+1, m):
                step(moon, moons[k])
            moon.apply_velocity()

        current = [[*moon.pos, *moon.velocity] for moon in moons]
        for i in range(3):
            is_cycle = matches_initial_state(initial_values, current, i, m)
            if is_cycle and cycles[i] is None:
                cycles[i] = counter
        
        if stop_cycles(cycles):
            print("Evrika")
            print(lcm(lcm(cycles[1], cycles[0]), cycles[2]))
            break

        counter += 1
    
    # print(compute_energy(moons))

def compute_energy(moons):
    total = 0
    for moon in moons:
        pot = sum([abs(x) for x in moon.pos])
        kin = sum([abs(x) for x in moon.velocity])
        total += pot * kin
    return total

if __name__ == "__main__":
    file_name = sys.argv[1]
    
    moons = []
    with open(file_name) as f:
        line = f.readline()
        index = 0
        while line:
            line = line.strip().replace("<", "").replace(">", "").split(',')
            x, y, z = [x.split('=') for x in line]
            pos = [int(x[1]), int(y[1]), int(z[1])]
            moons.append(Moon(pos))
            index += 1
            line = f.readline()

    apply_steps(moons)    
