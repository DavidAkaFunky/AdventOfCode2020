def part1(input) -> int:
    directions = ["E", "S", "W", "N"]
    route = {"N": 0, "S": 0, "E": 0, "W": 0}
    i = 0
    for line in input:
        currentDir = line[0]
        value = int(line[1:])
        if currentDir in directions:
            route[currentDir] += value
        elif currentDir == "F":
            route[directions[i]] += value
        else:
            rotation = value//90
            if currentDir == "L":
                rotation *= -1
            i = (i + rotation) % len(directions)
    return abs(route["E"] - route["W"]) + abs(route["N"] - route["S"])

def part2(input) -> int:
    directions = ["E", "S", "W", "N"]
    ship = {"N": 0, "S": 0, "E": 0, "W": 0}
    waypoint = {"N": 1, "S": 0, "E": 10, "W": 0}
    for line in input:
        currentDir = line[0]
        value = int(line[1:])
        if currentDir in directions:
            waypoint[currentDir] += value
        elif currentDir == "F":
            for dir in directions:
                ship[dir] += value * waypoint[dir]
        else:
            rotation = value//90
            if currentDir == "R":
                rotation *= -1
            from copy import deepcopy
            waypointCopy = deepcopy(waypoint)
            for i in range(len(directions)):
                waypoint[directions[i]] = waypointCopy[directions[(i + rotation) % len(directions)]]
    return abs(ship["E"] - ship["W"]) + abs(ship["N"] - ship["S"])


f = open("input.txt", "r")
input = f.read().splitlines()
print(part1(input)) #2228
print(part2(input)) #42908