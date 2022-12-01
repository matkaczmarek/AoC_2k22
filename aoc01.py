with open("./inputs/aoc01.in", 'r') as fp:
    elves = fp.readlines()

curr_count = 0
max_count = [0, 0, 0]
for e in elves:
    if e.strip("\n") == "":
        if curr_count > max_count[0]:
            max_count = [curr_count] + max_count[0:2]
        elif curr_count > max_count[1]:
            max_count = [max_count[0]] + [curr_count] + [max_count[1]]
        elif curr_count > max_count[2]:
            max_count = max_count[0:2] + [curr_count]
        curr_count = 0
    else:
        curr_count += int(e.strip("\n"))

print(sum(max_count))
