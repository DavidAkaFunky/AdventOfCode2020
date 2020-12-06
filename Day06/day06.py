def part1(input):
    reply = ""
    total = 0
    for line in input:
        if line != "":
            reply += line
        else:
            total += len(set(reply))
            reply = ""
    if reply != "":
        total += len(set(reply))
    return total

def part2(input):
    valid = ""
    total = 0
    first = True
    for line in input:
        if line != "":
            if first:
                valid = line
                first = False
            else:
                valid = set(valid).intersection(line)
        else:
            total += len(valid)
            valid = ""
            first = True
    if valid != "":
        total += len(valid)
    return total

f = open("input.txt", "r")
input = f.read().splitlines()
print(part1(input)) #6911
print(part2(input)) #3473
f.close()