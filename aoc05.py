with open("./inputs/aoc05.in", 'r') as fp:
    lines = fp.readlines()

i = 0
stacks = [[], [], [], [], [], [], [], [], []]
print(stacks)
while lines[i][1] != "1":
    line = lines[i]
    print(line)
    for j in range(9):
        if len(line) <= 1 + j*4:
            break
        letter = line[1 + j*4]
        if letter == ' ':
            continue

        stacks[j].insert(0, letter)
    i += 1

i += 2
print(stacks)
while i != len(lines):
    splitted = lines[i].split(" ")
    amount, start, end = int(splitted[1]), int(splitted[3])-1, int(splitted[5])-1
    temp_stack = []
    for j in range(amount):
        if len(stacks[start]) == 0:
            continue
        letter = stacks[start].pop()
        temp_stack.append(letter)

    while len(temp_stack) != 0:
        letter = temp_stack.pop()
        stacks[end].append(letter)
    i += 1

for i in range(9):
    print(stacks[i].pop(), end="")
