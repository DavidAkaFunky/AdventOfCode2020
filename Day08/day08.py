def part1(input) -> int:
    acc = 0
    line = 0
    checkedLines = []
    while line not in checkedLines:
        checkedLines.append(line)
        add = int(input[line][5:])
        if input[line][4] == "-":
            add *= -1
        if input[line][:3] == "jmp":
            line += add
        else:
            if input[line][:3] == "acc":
                acc += add
            line += 1
    return acc

def part2(input) -> int:
    from copy import deepcopy
    def isOutOfRange(input, numLine, newContent) -> (bool, int):
        newInput = deepcopy(input)
        newInput[numLine] = newContent + newInput[numLine][3:]
        acc = 0
        line = 0
        checkedLines = []
        while True:
            checkedLines.append(line)
            add = int(newInput[line][5:])
            if newInput[line][4] == "-":
                add *= -1
            if newInput[line][:3] == "jmp":
                line += add
            else:
                if newInput[line][:3] == "acc":
                    acc += add
                line += 1
            if line == len(newInput):
                return (True, acc)
            elif line > len(newInput) or line in checkedLines:
                return (False, acc)
    for line in range(len(input)):
        res = (False, 0)
        if input[line][:3] == "jmp":
            res = isOutOfRange(input, line, "nop")
        elif input[line][:3] == "nop":
            res = isOutOfRange(input, line, "jmp")
        if res[0]:
            return res[1]

f = open("input.txt", "r")
input = f.read().splitlines()
print(part1(input)) #1782
print(part2(input)) #797
f.close()