with open("./inputs/aoc08.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

n = len(lines)  # rows
m = len(lines[0])  # columns
visible_left = [[False] * m for _ in range(n)]
visible_right = [[False] * m for _ in range(n)]
visible_top = [[False] * m for _ in range(n)]
visible_bot = [[False] * m for _ in range(n)]

# left
for i in range(n):
    max_tree = -1
    for j in range(m):
        curr_tree = int(lines[i][j])
        if max_tree < curr_tree:
            max_tree = curr_tree
            visible_left[i][j] = True

# right
for i in range(n):
    max_tree = -1
    for j in range(m-1, -1, -1):
        curr_tree = int(lines[i][j])
        if max_tree < curr_tree:
            max_tree = curr_tree
            visible_right[i][j] = True

# top
for j in range(m):
    max_tree = -1
    for i in range(n):
        curr_tree = int(lines[i][j])
        if max_tree < curr_tree:
            max_tree = curr_tree
            visible_top[i][j] = True
# bot
for j in range(m):
    max_tree = -1
    for i in range(n-1, -1, -1):
        curr_tree = int(lines[i][j])
        if max_tree < curr_tree:
            max_tree = curr_tree
            visible_bot[i][j] = True

# count = 0
# for i in range(n):
#     for j in range(m):
#         if visible_left[i][j] or visible_right[i][j] or visible_top[i][j] or visible_bot[i][j]:
#             count += 1
#
# print(count)

visible_left_2 = [[0] * m for _ in range(n)]
visible_right_2 = [[0] * m for _ in range(n)]
visible_top_2 = [[0] * m for _ in range(n)]
visible_bot_2 = [[0] * m for _ in range(n)]

# left
for i in range(n):
    tree_dict = {x: 0 for x in range(10)}
    max_tree = (-1, 0)
    for j in range(m):
        curr_tree = int(lines[i][j])
        visible_left_2[i][j] = abs(j - tree_dict[curr_tree])
        for height in range(curr_tree, -1, -1):
            tree_dict[height] = j

# right
for i in range(n):
    tree_dict = {x: 0 for x in range(10)}
    max_tree = (-1, 0)
    for j in range(m-1, -1, -1):
        curr_tree = int(lines[i][j])
        visible_right_2[i][j] = abs(j - tree_dict[curr_tree])
        for height in range(curr_tree, -1, -1):
            tree_dict[height] = j

# top
for j in range(m):
    tree_dict = {x: 0 for x in range(10)}
    max_tree = (-1, 0)
    for i in range(n):
        curr_tree = int(lines[i][j])
        visible_top_2[i][j] = abs(i - tree_dict[curr_tree])
        for height in range(curr_tree, -1, -1):
            tree_dict[height] = i

# bot
for j in range(m):
    tree_dict = {x: 0 for x in range(10)}
    max_tree = (-1, 0)
    for i in range(n-1, -1, -1):
        curr_tree = int(lines[i][j])
        visible_bot_2[i][j] = abs(i - tree_dict[curr_tree])
        for height in range(curr_tree, -1, -1):
            tree_dict[height] = i

for i in range(n):
    for j in range(m):
        if visible_left[i][j]:
            visible_left_2[i][j] = j
        if visible_right[i][j]:
            visible_right_2[i][j] = m-1-j
        if visible_top[i][j]:
            visible_top_2[i][j] = i
        if visible_bot[i][j]:
            visible_bot_2[i][j] = n-1-i



max_range = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        max_range = max(max_range, visible_left_2[i][j] * visible_right_2[i][j] * visible_top_2[i][j] * visible_bot_2[i][j])

print(max_range)
