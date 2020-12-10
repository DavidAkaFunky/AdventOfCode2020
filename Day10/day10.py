def part1(input) -> int:
    count1 = count3 = 0
    for i in range(len(input) - 1):
        if input[i+1] - input[i] == 1:
            count1 += 1
        elif input[i+1] - input[i] == 3:
            count3 += 1
    return count1 * count3

def part2(input) -> int:
    #TO DO
    def possibleArrangements(input, lst, i):
        if i == len(input) - 1:
            print(lst)
            return lst
        j = i + 1
        res = []
        while input[j] - input[i] <= 3 and j < len(input):
            res += [possibleArrangements(input, lst + [input[j]], j)]
            j += 1
        return res
    res = possibleArrangements(input, [], 0)
    return len(res)

f = open("input.txt", "r")
input = f.read().splitlines()
for i in range(len(input)):
    input[i] = int(input[i])
input.append(0)
input.sort()
input.append(input[len(input)-1] + 3)
print(part1(input)) #2310
print(part2(input))
