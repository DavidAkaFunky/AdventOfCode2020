def part1(input) -> int:
    def testSeats(input, type, centreX, centreY, minX, maxX, minY, maxY, threshold) -> bool:
        count = 0
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                if not (x == centreX and y == centreY):
                    if input[x][y] == type:
                        count += 1
        print(count >= threshold)
        return count >= threshold
    from copy import deepcopy
    while True:
        new_input = deepcopy(input)
        for i in range(len(input)):
            minX, maxX = i-1, i+1
            if i == 0:
                minX = 0
            if i == len(input) - 1:
                maxX = len(input) - 1
            new_input[i] = list(new_input[i])
            for j in range(len(input[i])):
                minY, maxY = j-1, j+1
                if j == 0:
                    minY = 0
                if j == len(input[i]) - 1:
                    maxY = len(input[i]) - 1
                if input[i][j] == "L" and testSeats(input, "L", i, j, minX, maxX, minY, maxY, 1):
                    new_input[i][j] = "#"
                elif input[i][j] == "#" and testSeats(input, "#", i, j, minX, maxX, minY, maxY, 4):
                    new_input[i][j] = "L"
            new_input[i] = ''.join(new_input[i])
            print(new_input)
        print("_______")
        if new_input == input:
            break
        else:
            input = new_input
    count = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "L":
                count += 1
    return count


f = open("input2.txt", "r")
input = f.read().splitlines()
print(part1(input))