def part1(input):
    for i in input:
        for j in input:
            if i + j == 2020:
                return i * j

def part2(input):
    for i in input:
        for j in input:
            for k in input:
                if i + j + k == 2020:
                    return i * j * k

f = open("input.txt", "r")
input = f.readlines()
for i in range(len(input)):
    input[i] = int(input[i])
print(part1(input)) #605364
print(part2(input)) #128397680
f.close()