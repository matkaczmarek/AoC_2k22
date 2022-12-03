with open("./inputs/aoc03.in", 'r') as fp:
    lines = fp.readlines()

# out = 0
# for line in lines:
#     first, second = line[:len(line)//2], line[len(line)//2:]
#     print(first)
#     items_1 = set(first)
#     items_2 = set(second)
#     letter = list(items_1 & items_2)[0]
#     if letter.islower():
#         out += ord(letter) - ord('a') + 1
#     else:
#         out += ord(letter) - ord('A') + 27

out = 0
for i in range(0, len(lines), 3):
    first, second, third = lines[i].strip("\n"), lines[i+1].strip("\n"), lines[i+2].strip("\n")
    items_1 = set(first)
    items_2 = set(second)
    items_3 = set(third)
    letter = list(items_1 & items_2 & items_3)[0]
    if letter.islower():
        out += ord(letter) - ord('a') + 1
    else:
        out += ord(letter) - ord('A') + 27

print(out)

