import sys

with open("./inputs/aoc14.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

coordinates = []
max_x = 0
min_x = 500
max_y = 0
min_y = 0
for line in lines:
    splitted = line.split(" -> ")
    single_rock = []
    for s in splitted:
        x, y = map(int, s.split(","))
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        single_rock.append((x, y))
    coordinates.append(single_rock)

grid = []
for i in range(max_y+3):
    grid.append(['.' for j in range(max_x+1000)])

grid.pop()
grid.append(['#' for j in range(max_x+1000)])
#print(grid)


def draw_horizontal(start_x, stop_x, y):
    global grid
    for i in range(start_x, stop_x+1):
        grid[y][i] = '#'

def draw_vertical(start_y, stop_y, x):
    global grid
    for i in range(start_y, stop_y+1):
        grid[i][x] = '#'


for cord in coordinates:
    for i in range(len(cord) - 1):
        first = cord[i]
        second = cord[i+1]
        if first[0] == second[0]:
            draw_vertical(min(first[1], second[1]), max(first[1], second[1]), first[0])
        else:
            draw_horizontal(min(first[0], second[0]), max(first[0], second[0]), first[1])

out = 0
curr_x = 500
curr_y = 0

def move_sand():
    global grid, curr_x, curr_y
    if grid[curr_y+1][curr_x] == '.':
        grid[curr_y][curr_x] = '.'
        grid[curr_y+1][curr_x] = 'o'
        curr_y += 1
        return True

    if grid[curr_y+1][curr_x-1] == '.':
        grid[curr_y][curr_x] = '.'
        grid[curr_y+1][curr_x-1] = 'o'
        curr_x -= 1
        curr_y += 1
        return True

    # print(max_x, curr_x, max_y, curr_y)
    if grid[curr_y+1][curr_x+1] == '.':
        grid[curr_y][curr_x] = '.'
        grid[curr_y+1][curr_x+1] = 'o'
        curr_x += 1
        curr_y += 1
        return True

    return False

# while True:
#     curr_x = 500
#     curr_y = 0
#     try:
#         while move_sand():
#             pass
#
#         out += 1
#     except:
#         break
#
# print(out)

while True:
    if not move_sand():
        if curr_x == 500 and curr_y == 0:
            break
        curr_x = 500
        curr_y = 0
        out += 1
        continue

print(out + 1)

