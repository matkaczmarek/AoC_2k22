with open("inputs/aoc10.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

# def check_signal(cycle_num, X):
#     if cycle_num in [20, 60, 100, 140, 180, 220]:
#         return X * cycle_num
#
#     return 0

# cycle_num = 0
# X = 1
# out = 0
# for line in lines:
#     splitted = line.split(" ")
#     if splitted[0] == "noop":
#         cycle_num += 1
#         out += check_signal(cycle_num, X)
#         continue
#     elif splitted[0] == "addx":
#         cycle_num += 1
#         out += check_signal(cycle_num, X)
#         cycle_num += 1
#         out += check_signal(cycle_num, X)
#         X += int(splitted[1])

# print(out)

def generate_pixel(sprite_pos, cycle_num):
    if cycle_num % 40 in range(sprite_pos-1, sprite_pos+2):
        return '#'
    else:
        return "."

cycle_num = 0
sprite_position = 1
displayed_row = ""
out = []
for line in lines:
    splitted = line.split(" ")
    if splitted[0] == "noop":
        if cycle_num % 40 == 0 and cycle_num != 0:
            out.append(displayed_row)
            displayed_row = ""
        displayed_row += generate_pixel(sprite_position, cycle_num)
        cycle_num += 1
        continue
    elif splitted[0] == "addx":
        if cycle_num % 40 == 0 and cycle_num != 0:
            out.append(displayed_row)
            displayed_row = ""
        displayed_row += generate_pixel(sprite_position, cycle_num)
        cycle_num += 1

        if cycle_num % 40 == 0 and cycle_num != 0:
            out.append(displayed_row)
            displayed_row = ""
        displayed_row += generate_pixel(sprite_position, cycle_num)
        cycle_num += 1

        sprite_position += int(splitted[1])

for row in out:
    print(row)
print(displayed_row)