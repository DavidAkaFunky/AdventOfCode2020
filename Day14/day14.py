def part1(input) -> int:
    dic = {}
    for line in input:
        line = line.split()
        line.pop(1)
        key = line[0]
        value = line[1]
        if key == "mask":
            mask = {}
            for i in range(len(value)):
                if value[i] != "X":
                    mask[i] = value[i]
        else:
            index = key[4:-1]
            value = bin(int(value))[2:]
            value = list((36-len(value)) * "0" + value)
            for i in mask:
                value[i] = mask[i]
            dic[index] = int("".join(value), 2)
    total = 0
    for el in dic:
        total += dic[el]
    return total

def part2(input) -> int:
    dic = {}
    indexes = []
    for line in input:
        line = line.split()
        line.pop(1)
        key = line[0]
        value = line[1]
        if key == "mask":
            key = bin(int(key))[2:]
            key = list((36-len(key)) * "0" + key)
        else:
            for index in indexes:
                dic[index] = int(value)
    total = 0
    for el in dic:
        total += dic[el]
    return total


f = open("input.txt", "r")
input = f.read().splitlines()
print(part1(input)) #16003257187056
#print(part2(input))