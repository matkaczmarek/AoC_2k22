with open("./inputs/aoc18.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

# cubes_to_neigh = {}
# for line in lines:
#     x, y, z = map(int, line.split(','))
#     cubes_to_neigh[(x, y, z)] = []

# add = [-1, 1]
# for cube in cubes_to_neigh.keys():
#     x, y, z = cube
#     for a in add:
#         if (x+a, y, z) in cubes_to_neigh.keys():
#             cubes_to_neigh[cube].append((x+a, y, z))
#
#         if (x, y+a, z) in cubes_to_neigh.keys():
#             cubes_to_neigh[cube].append((x, y+a, z))
#
#         if (x, y, z+a) in cubes_to_neigh.keys():
#             cubes_to_neigh[cube].append((x, y, z+a))

# out = 0
# for cube in cubes_to_neigh.keys():
#     out += 6 - len(cubes_to_neigh[cube])
#
# print(out)

maximum = 30
droplets = set()
droplets_to_neigh = {}

for line in lines:
    x, y, z = map(int, line.split(','))
    droplets.add((x, y, z))
    droplets_to_neigh[(x, y, z)] = []


def check_closed(x, y, z, opened):
    global maximum, droplets
    if (x, y, z) in droplets:
        return True

    if (x, y, z) in opened:
        return False

    check_x = [False, False]
    check_y = [False, False]
    check_z = [False, False]
    for x_prim in range(x-1, -2, -1):
        if (x_prim, y, z) in droplets:
            check_x[0] = True
            break
        elif (x_prim, y, z) in opened:
            break

    for x_prim in range(x+1, maximum):
        if (x_prim, y, z) in droplets:
            check_x[1] = True
            break
        elif (x_prim, y, z) in opened:
            break

    for y_prim in range(y-1, -2, -1):
        if (x, y_prim, z) in droplets:
            check_y[0] = True
            break
        elif (x, y_prim, z) in opened:
            break

    for y_prim in range(y+1, maximum):
        if (x, y_prim, z) in droplets:
            check_y[1] = True
            break
        elif (x, y_prim, z) in opened:
            break

    for z_prim in range(z-1, -2, -1):
        if (x, y, z_prim) in droplets:
            check_z[0] = True
            break
        elif (x, y, z_prim) in opened:
            break


    for z_prim in range(z+1, maximum):
        if (x, y, z_prim) in droplets:
            check_z[1] = True
            break
        elif (x, y, z_prim) in opened:
            break

    return check_x[0] and check_x[1] and check_y[0] and check_y[1] and check_z[0] and check_z[1]

opened = set()
prev_size = -1
while prev_size != len(opened):
    prev_size = len(opened)
    for x in range(-2, maximum):
        for y in range(-2, maximum):
            for z in range(-2, maximum):
                if not check_closed(x, y, z, opened):
                    opened.add((x, y, z))

out = 0
add = [-1, 1]
for droplet in droplets:
    x, y, z = droplet
    for a in add:
        if (x+a, y, z) in opened:
            out += 1

        if (x, y+a, z) in opened:
            out += 1

        if (x, y, z+a) in opened:
            out += 1

print(out)