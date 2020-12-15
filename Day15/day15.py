def day15(input, dic, limit) -> int:
    former = input[-1]
    for i in range(len(input), limit):
        if len(dic[former]) == 1:
            former = 0
        else:
            former = dic[former][-1] - dic[former][-2]
        try:
            dic[former].append(i)
        except KeyError:
            dic[former] = [i]
    return former

input = [6,4,12,1,20,0,16]
dic = {}
for i in range(len(input)):
    dic[input[i]] = [i]
from copy import deepcopy
print(day15(input, deepcopy(dic), 2020)) #475
print(day15(input, deepcopy(dic), 30000000)) #11261