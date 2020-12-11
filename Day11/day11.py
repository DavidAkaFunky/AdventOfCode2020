def part1(input) -> int:

    def testSeats(input, centreX, centreY, minX, maxX, minY, maxY, threshold) -> bool:
        count = 0
        for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                if not (x == centreX and y == centreY):
                    if input[y][x] == "#":
                        count += 1
                        if count >= threshold:
                            return True
        return False

    from copy import deepcopy
    count = 0

    while True:
        new_input = deepcopy(input)

        for i in range(len(input)):
            minY, maxY = i-1, i+1
            if i == 0:
                minY = 0
            if i == len(input) - 1:
                maxY = len(input) - 1
            new_input[i] = list(new_input[i])

            for j in range(len(input[i])):
                minX, maxX = j-1, j+1
                if j == 0:
                    minX = 0
                if j == len(input[i]) - 1:
                    maxX = len(input[i]) - 1
                if input[i][j] == "L" and not testSeats(input, j, i, minX, maxX, minY, maxY, 1):
                    new_input[i][j] = "#"
                    count += 1
                elif input[i][j] == "#" and testSeats(input, j, i, minX, maxX, minY, maxY, 4):
                    new_input[i][j] = "L"
                    count -= 1

            new_input[i] = ''.join(new_input[i])

        if new_input == input:
            break

        else:
            input = new_input

    return count

def part2(input) -> int:

    def testSeats(input, centreX, centreY, threshold) -> bool:

        def findSeat(addX, addY) -> int:
            x, y = centreX + addX, centreY + addY
            while 0 <= y < len(input) and 0 <= x < len(input[y]):
                if input[y][x] == "#":
                    return 1
                elif input[y][x] == "L":
                    return 0
                x += addX
                y += addY
            return 0

        adds = (-1, 0, 1)    
        count = 0
        for i in adds:
            for j in adds:
                if (i,j) != (0,0):
                    count += findSeat(i, j)
        if count >= threshold:
            return True
        return False

    from copy import deepcopy
    count = 0

    while True:
        new_input = deepcopy(input)

        for i in range(len(input)):
            new_input[i] = list(new_input[i])

            for j in range(len(input[i])):
                if input[i][j] == "L" and not testSeats(input, j, i, 1):
                    new_input[i][j] = "#"
                    count += 1
                elif input[i][j] == "#" and testSeats(input, j, i, 5):
                    new_input[i][j] = "L"
                    count -= 1

            new_input[i] = ''.join(new_input[i])

        if new_input == input:
            break

        else:
            input = new_input
            
    return count


f = open("input.txt", "r")
input = f.read().splitlines()
print(part1(input))
print(part2(input))