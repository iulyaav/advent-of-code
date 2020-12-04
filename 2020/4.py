import re

class Passport:

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.hcl = hcl
        self.hgt = hgt
        self.eyr = eyr
        self.iyr = iyr
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def validate_a(self):
        if self.byr is None or self.hcl is None or self.hgt is None or self.eyr is None or self.iyr is None:
            return False
        if self.ecl is None or self.pid is None:
            return False
        return True
    
    def validate_height(self):
        if self.hgt is None:
            return False
        if self.hgt[-2:] == "cm" and int(self.hgt[:-2]) >= 150 and int(self.hgt[:-2]) <= 193:
            return True
        elif self.hgt[-2:] == "in" and int(self.hgt[:-2]) >= 59 and int(self.hgt[:-2]) <= 76:
            return True
        return False
    
    def validate_hair_color(self):
        if self.hcl is None:
            return False
        matched = re.match("^#[0-9|a-f]{6}$", self.hcl)
        return bool(matched)
    
    def validate_eye_color(self):
        return self.ecl is not None and self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
    def validate_pid(self):
        return self.pid is not None and self.pid.isdigit() and len(self.pid) == 9
        

    
    def validate_b(self):
        if self.byr is None or int(self.byr) < 1920 or int(self.byr) > 2002:
            return False
        if self.iyr is None or int(self.iyr) < 2010 or int(self.iyr) > 2020:
            return False
        if self.eyr is None or int(self.eyr) < 2020 or int(self.eyr) > 2030:
            return False
        return self.validate_height() and self.validate_hair_color() and self.validate_eye_color() and self.validate_pid()


def four_a():
    with open("input_4.txt", "r") as f:
        counter = 0
        line = f.readline()
        passport = {}
        counter = 0
        while line:
            if line == "\n":
                p = Passport(**passport)
                if p.validate_a():
                    counter += 1
                passport = {}
            else:
                fields = line.split(' ')
                for field in fields:
                    name = field.split(":")[0]
                    passport[name] = "wee"
            line =f.readline()
        return counter


def four_b():
    with open("input_4.txt", "r") as f:
        counter = 0
        line = f.readline()
        passport = {}
        counter = 0
        while line:
            if line == "\n":
                p = Passport(**passport)
                if p.validate_b():
                    counter += 1
                passport = {}
            else:
                fields = line.split(' ')
                for field in fields:
                    name, val = field.strip().split(":")
                    passport[name] = val
            line =f.readline()
        return counter


print(four_b())