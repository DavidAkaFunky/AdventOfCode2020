def part01(input, slope_right, slope_down):
    total = 0
    pos = 0
    for i in range(0, len(input), slope_down):
        if input[i][pos] == "#":
            total += 1
        pos = (pos + slope_right) % len(input[i])
    return total

def part02(input):
    return part01(input, 1, 1) * part01(input, 3, 1) * part01(input, 5, 1) * part01(input, 7, 1) * part01(input, 1, 2)

f = open("input.txt")
input = f.read().splitlines()
print(part01(input, 3, 1))
print(part02(input))