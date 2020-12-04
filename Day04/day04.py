def part1(input):
    total = 0
    for passport in input:
        if len(passport) == 8 or len(passport) == 7 and "cid" not in passport:
            total += 1
    return total

def part2(input):
    def isValid(passport):
        if len(passport) == 8 or len(passport) == 7 and "cid" not in passport:
            try:
                byr = int(passport["byr"])
                if byr < 1920 or byr > 2002:
                    return False
                iyr = int(passport["iyr"])
                if iyr < 2010 or iyr > 2020:
                    return False
                eyr = int(passport["eyr"])
                if eyr < 2020 or eyr > 2030:
                    return False
                hgt = passport["hgt"]
                valid = False
                if len(hgt) == 5 and hgt[3:] == "cm":
                    value = int(hgt[:3])
                    if value < 150 or value > 193:
                        return False
                    valid = True
                elif len(hgt) == 4 and hgt[2:] == "in":
                    value = int(hgt[:2])
                    if value < 59 or value > 76:
                        return False
                    valid = True
                if not valid:
                    return False
                hcl = passport["hcl"]
                validNumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                valid = False
                if len(hcl) == 7 and hcl[0] == "#":
                    validChars = validNumbers + ["a", "b", "c", "d", "e", "f"]
                    for i in range(1,len(hcl)):
                        if hcl[i] not in validChars:
                            return False
                    valid = True
                if not valid:
                    return False
                ecl = passport["ecl"]
                if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    return False
                pid = passport["pid"]
                valid = False
                if len(pid) == 9:
                    for char in pid:
                        if char not in validNumbers:
                            print("pid1")
                            return False
                    valid = True
                if not valid:
                    return False
                return True
            except ValueError:
                return False
            except TypeError:
                return False
        return False
    total = 0
    for passport in input:
        if isValid(passport):
            total += 1
    return total


f = open("input.txt", "r")
input = f.read().splitlines()
passports = []
passport = {}
for line in input:
    if line != "":
        part = dict(x.split(":") for x in line.split())
        passport = {**passport, **part}
    else:
        passports.append(passport)
        passport = {}
passports.append(passport)
print(part1(passports)) #250
print(part2(passports)) #158
f.close()