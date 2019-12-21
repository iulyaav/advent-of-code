import sys
from collections import OrderedDict, Counter, defaultdict

class Ingredient:

    def __init__(self, name, batch, ingredients):
        self.name = name
        self.batch = batch
        self.ingredients = ingredients
        self.ore = None

    def __repr__(self):
        return f"{self.name} = {self.ingredients}"


def cookbook(data):
    c = {}
    for d in data.strip().split('\n'):
        left, right = [x.strip() for x in d.strip().split("=>")]
        batch, name = right.strip().split(' ')
        ingredients = left.strip().split(',')
        c[name] = Ingredient(name, int(batch), ingredients)
    return c


def make_fuel(reactions, element='FUEL', qty=1, cache=None):
    if cache is None:
        cache = {}
    
    if any('ORE' in x for x in reactions[element].ingredients):
        if element in cache:
            cache[element] += qty
        else:
            cache[element] = qty
    
    else:
        print(f"Making {element}")
        next_ingredients = reactions[element].ingredients

        for ingredient in next_ingredients:
            qty, name = ingredient.strip().split(' ')
            cache = {**cache, **make_fuel(reactions, element=name, qty=int(qty), cache=cache)}
    
    return cache




if __name__ == "__main__":
    file_name = sys.argv[1]
    file_data = None
    with open(file_name) as f:
        file_data = f.read()
    
    reactions  = cookbook(file_data)
    print(reactions)
    c = make_fuel(reactions)
    print(c)