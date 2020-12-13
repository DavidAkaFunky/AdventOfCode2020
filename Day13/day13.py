def part1(startTime, buses) -> int:
    from math import ceil
    activeBuses = list(filter(lambda x: x != "x", buses))
    for i in range(len(activeBuses)):
        value = ceil(startTime/activeBuses[i]) * activeBuses[i]
        if i == 0 or (i != 0 and value < minTime):
            minTime = value
            minBus = activeBuses[i]
    return minBus * (minTime - startTime)

def part2(buses) -> int:
    from sympy.ntheory.modular import crt
    activeBuses = []
    remainders = []
    for i in range(len(buses)):
        if buses[i] != "x":
            activeBuses.append(buses[i])
            remainders.append(-i)
    return crt(activeBuses, remainders)[0]

f = open("input.txt", "r")
input = f.read().splitlines()
startTime = int(input[0])
buses = input[1].split(",")
for i in range(len(buses)):
    try:
        buses[i] = int(buses[i])
    except ValueError:
        pass
print(part1(startTime, buses)) #3789
print(part2(buses)) #667437230788118