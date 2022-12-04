with open("./inputs/aoc04.in", 'r') as fp:
    lines = fp.readlines()

out = 0
for line in lines:
    first, second = line.strip("\n").split(",")
    start_1, end_1 = first.split("-")
    start_2, end_2 = second.split("-")
    start_1, end_1 = int(start_1), int(end_1)
    start_2, end_2 = int(start_2), int(end_2)

    # if end_1 - start_1 >= end_2 - start_2:
    #     if end_1 >= end_2 and start_1 <= start_2:
    #         out += 1
    # else:
    #     if end_1 <= end_2 and start_1 >= start_2:
    #         out += 1

    if start_1 <= start_2:
        if start_2 <= end_1:
            out += 1
    elif start_2 <= start_1:
        if start_1 <= end_2:
            out += 1

print(out)