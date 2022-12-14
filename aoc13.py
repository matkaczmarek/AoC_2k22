import json
from functools import cmp_to_key

with open("./inputs/aoc13.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

def compare_lines(first, second):
    if type(first) is int and type(second) is int:
        if first < second:
            return -1
        elif first > second:
            return 1
        else:
            return 0

    if type(first) is list and type(second) is list:
        for i in range(max(len(first), len(second))):
            try:
                res = compare_lines(first[i], second[i])
            except:
                if len(first) < len(second):
                    return -1
                elif len(first) > len(second):
                    return 1
                else:
                    return 0

            if res != 0:
                return res

    if type(first) is int:
        return compare_lines([first], second)

    if type(second) is int:
        return compare_lines(first, [second])

    return 0

# out = 0
# index = 1
# i = 0
# while i < len(lines):
#     first = json.loads(lines[i])
#     second = json.loads(lines[i+1])
#     # print(index, first, second, compare_lines(first, second))
#     if compare_lines(first, second) == -1:
#         out += index
#
#     index += 1
#     i += 3
#
# print(out)

lines = [json.loads(line) for line in lines if len(line) != 0]
lines.append([2])
lines.append([[6]])
sorted_lines = sorted(lines, key=cmp_to_key(compare_lines))
print((sorted_lines.index([2])+1) * (sorted_lines.index([[6]])+1))
