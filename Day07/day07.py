def part1(input) -> int:
    total = 0
    carriers = ["shiny gold"]
    added = 0
    while True:
        for line in input:
            splittedLine = line.split()
            name = splittedLine[0] + " " + splittedLine[1]
            if name not in carriers:
                for carrier in carriers:
                    if carrier in line:
                        total += 1
                        added += 1
                        carriers.append(name)
                        break
        if added == 0:
            break
        else:
            added = 0
    return total

def part2(input) -> int:
    def calculateTotalBags(bags, name) -> int:
        if bags[name] == {}:
            return 0
        else:
            total = 0
            for bag in bags[name]:
                total += (1 + calculateTotalBags(bags, bag)) * bags[name][bag]
            return total
    bags = {}
    for line in input:
        line = line.split()
        name = line[0] + " " + line[1]
        bags[name] = {}
        if "no" not in line:
            for i in range(4, len(line), 4):
                content = line[i+1] + " " + line[i+2]
                bags[name][content] = int(line[i])
    return calculateTotalBags(bags, "shiny gold")
    
    

f = open("input.txt", "r")
input = f.read().splitlines()
print(part1(input)) #378
print(part2(input)) #27526
f.close()