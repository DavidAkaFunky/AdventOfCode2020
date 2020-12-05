def calculateSeat(line, numRows, numColumns):
    def getSeatParameter(line, up, down, currentCharNum, numChars, minValue, maxValue):
        if line[currentCharNum] == up:
            if currentCharNum == numChars:
                return maxValue
            currentCharNum += 1
            return getSeatParameter(line, up, down, currentCharNum, numChars, (minValue + maxValue) // 2 + 1, maxValue)
        elif line[currentCharNum] == down:
            if currentCharNum == numChars:
                return minValue
            currentCharNum += 1
            return getSeatParameter(line, up, down, currentCharNum, numChars, minValue, (minValue + maxValue) // 2)
    return getSeatParameter(line, "B", "F", 0, numRows - 1, 0, 2 ** numRows - 1) * (numRows + 1) + getSeatParameter(line, "R", "L", numRows, numRows + numColumns - 1, 0, 2 ** numColumns - 1)

def part1(input):
    max = 0
    for line in input:
        seat = calculateSeat(line, 7, 3)
        if seat > max:
           max = seat
    return max

def part2(input):
    places = []
    for line in input:
        places.append(calculateSeat(line, 7, 3))
    places.sort()
    for i in range(len(places) - 1):
        if places[i] + 2 == places[i + 1]:
            return places[i] + 1


f = open("input.txt", "r")
input = f.read().splitlines()
print(part1(input)) #890
print(part2(input)) #651
f.close()