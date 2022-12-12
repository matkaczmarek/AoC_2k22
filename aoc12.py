import sys
from queue import PriorityQueue

with open("./inputs/aoc12.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

lines_temp = []
for line in lines:
    lines_temp.append(list(line))
lines = lines_temp


def is_adjacent(left, right):
    if ord(left) >= ord(right):
        return True

    return abs(ord(left) - ord(right)) <= 1

def add_tuple(left, right):
    return (left[0] + right[0], left[1] + right[1])

elevation_a = []
vertices = []
edges = {}
moves = {(1, 0), (0, 1), (-1, 0), (0, -1)}
n = len(lines)
m = len(lines[0])
for i in range(n):
    for j in range(m):
        vertices.append((i, j))
        edges[(i, j)] = []
        if lines[i][j] == 'S' or lines[i][j] == 'a':
            elevation_a.append((i, j))

        if lines[i][j] == 'S':
            start_point = (i, j)
            lines[i][j] = 'a'
        elif lines[i][j] == 'E':
            end_point = (i, j)
            lines[i][j] = 'z'

for i in range(n):
    for j in range(m):
        for move in moves:
            x, y = add_tuple((i, j), move)
            if x < 0 or x >= n or y < 0 or y >= m:
                continue

            if is_adjacent(lines[i][j], lines[x][y]):
                    edges[(i, j)].append((x, y))

def dikstra(start_point, end_point, vertices, edges):
    visited = {v: False for v in vertices}
    distances = {v: 0 for v in vertices}
    queue = PriorityQueue()
    queue.put((0, start_point))
    while not queue.empty():
        dist, curr_v = queue.get()
        if visited[curr_v]:
            continue
        visited[curr_v] = True
        distances[curr_v] = dist

        for neigh in edges[curr_v]:
            if visited[neigh]:
                continue

            queue.put((dist+1, neigh))

    return distances[end_point]

mini = sys.maxsize
for s in elevation_a:
    steps = dikstra(s, end_point, vertices, edges)
    if steps != 0:
        mini = min(mini, steps)

print(mini)

