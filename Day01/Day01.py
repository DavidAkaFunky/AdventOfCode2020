def part1(file):
    f = open(file)
    input = f.readlines()
    for i in input:
        for j in input:
            i = int(i)
            j = int(j)
            if i != j and i + j == 2020:
                return i * j

def part2(file):
    f = open(file)
    input = f.readlines()
    for i in input:
        for j in input:
            for k in input:
                i = int(i)
                j = int(j)
                k = int(k)
                if i != j and i != k and j != k and i + j + k == 2020:
                    return i * j * k
            
print(part1("input.txt"))
print(part2("input.txt"))