def part1(input) -> int:
    count1 = count3 = 0
    for i in range(len(input) - 1):
        if input[i+1] - input[i] == 1:
            count1 += 1
        elif input[i+1] - input[i] == 3:
            count3 += 1
    return count1 * count3

def part2(input) -> int:
    valid = {}
    def possibleArrangements(input) -> int:
        if len(input) <= 1:
            return 1
        if input[0] in valid:
            return valid[input[0]]
        i = 1
        res = 0
        while i < len(input) and input[i] - input[0] <= 3:
            res += possibleArrangements(input[i:])
            i += 1
        valid[input[0]] = res
        return res
    return possibleArrangements(input)

f = open("input.txt", "r")
input = f.read().splitlines()
for i in range(len(input)):
    input[i] = int(input[i])
input.append(0)
input.sort()
input.append(input[-1] + 3)
print(part1(input)) #2310
print(part2(input)) #64793042714624