def part1(input, preamble) -> int:
    possibleSums = []
    i = 0
    j = 0
    while i < preamble:
        for k in range(1, preamble):
            possibleSums.append(input[i] + input[k])
        i += 1
    while input[i] in possibleSums and i < len(input):
        possibleSums = possibleSums[preamble-1:]
        j += 1
        for k in range(j, i):
            possibleSums.append(input[k] + input[i])
        i += 1
    return input[i]

def part2(input, preamble, invalid) -> int:
    def getSumSmallestAndBiggest(input, min, max) -> (int, int, int):
        total = 0
        smallest = biggest = input[min]
        for i in range(min, max + 1):
            value = input[i]
            total += value
            if value < smallest:
                smallest = value
            elif value > biggest:
                biggest = value
        return (total, smallest, biggest)
    for i in range (1, len(input)):
        for j in range (i + 1, len(input)):
            output = getSumSmallestAndBiggest(input, i, j) 
            if output[0] == invalid:
                print(output[1], output[2])
                return output[1] + output[2]

f = open("input.txt", "r")
input = f.read().splitlines()
for i in range(len(input)):
    input[i] = int(input[i])
invalid = part1(input, 25)
print(invalid)
print(part2(input, 25, invalid))
f.close()