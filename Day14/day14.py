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
    for line in input:
        line = line.split()
        line.pop(1)
        key = line[0]
        value = line[1]
        if key == "mask":
            count = 0
            Xplaces = []
            for i in range(len(value)):
                if value[i] == "X":
                    count += 1
                    Xplaces.append(i)
            mask = list(value)
            for place in Xplaces:
                mask[place] = "0"
            mask = "".join(mask)
            
        else:
            index = int(key[4:-1])
            index = bin(index | int(mask,2))[2:]
            indexList = list((36-len(index)) * "0" + index)
            for i in range(2**count):
                binI = bin(i)[2:]
                binI = (count-len(binI)) * "0" + binI
                for j in range(count):
                    indexList[Xplaces[j]] = binI[j]
                index = "".join(indexList)
                dic[int(index,2)] = int(value)

    total = 0
    for el in dic:
        total += dic[el]
    return total


f = open("input.txt", "r")
input = f.read().splitlines()
print(part1(input)) #16003257187056
print(part2(input)) #3219837697833