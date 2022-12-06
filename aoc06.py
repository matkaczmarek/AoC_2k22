with open("./inputs/aoc06.in", 'r') as fp:
    line = fp.readlines()[0]

i = 0
while len(set(line[i:i+14])) != 14:
    i += 1

print(i + 14)
