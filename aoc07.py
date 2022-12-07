with open("./inputs/aoc07.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

sizes = {}
dir_stack = []

# i = 0
# while i < len(lines):
#     splitted = lines[i].split(" ")
#     if splitted[0] == "$":
#         if splitted[1] == "cd":
#             if splitted[2] == "..":
#                 dir_stack.pop()
#             elif splitted[2] == "/":
#                 dir_stack = ["/"]
#             else:
#                 dir_stack.append(splitted[2])
#
#         if splitted[1] == "ls":
#             i += 1
#             while i < len(lines) and lines[i][0] != "$":
#                 splitted_2 = lines[i].split(" ")
#                 if splitted_2[0] != "dir":
#                     pwd = ""
#                     for dir in dir_stack:
#                         pwd += "/" + dir
#                         if pwd in sizes:
#                             sizes[pwd] += int(splitted_2[0])
#                         else:
#                             sizes[pwd] = int(splitted_2[0])
#                 i += 1
#             continue
#     i += 1
#
# print(sum([x for x in sizes.values() if x <= 100000]))

i = 0
while i < len(lines):
    splitted = lines[i].split(" ")
    if splitted[0] == "$":
        if splitted[1] == "cd":
            if splitted[2] == "..":
                dir_stack.pop()
            elif splitted[2] == "/":
                dir_stack = ["/"]
            else:
                dir_stack.append(splitted[2])

        if splitted[1] == "ls":
            i += 1
            while i < len(lines) and lines[i][0] != "$":
                splitted_2 = lines[i].split(" ")
                if splitted_2[0] != "dir":
                    pwd = ""
                    for dir in dir_stack:
                        pwd += "/" + dir
                        if pwd in sizes:
                            sizes[pwd] += int(splitted_2[0])
                        else:
                            sizes[pwd] = int(splitted_2[0])
                i += 1
            continue
    i += 1

free_space = 70000000 - sizes["//"]
print(min([value for value in sizes.values() if free_space + value >= 30000000]))


