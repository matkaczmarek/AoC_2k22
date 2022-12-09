with open("./inputs/aoc09.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

# head_pos = (0, 0)
# tail_pos = (0, 0)
# tail_visited = set()
# tail_visited.add((0, 0))
#
# def is_adjacent(head, tail):
#     return tail[0] in range(head[0]-1, head[0]+2) and tail[1] in range(head[1]-1, head[1]+2)
#
# for line in lines:
#     direction, moves_num = line.split(" ")
#     moves_num = int(moves_num)
#     if direction == "U":
#         for i in range(moves_num):
#             head_pos = (head_pos[0], head_pos[1]+1)
#             if not is_adjacent(head_pos, tail_pos):
#                 tail_pos = (head_pos[0], head_pos[1]-1)
#                 tail_visited.add(tail_pos)
#
#     if direction == "D":
#         for i in range(moves_num):
#             head_pos = (head_pos[0], head_pos[1]-1)
#             if not is_adjacent(head_pos, tail_pos):
#                 tail_pos = (head_pos[0], head_pos[1]+1)
#                 tail_visited.add(tail_pos)
#
#     if direction == "L":
#         for i in range(moves_num):
#             head_pos = (head_pos[0]-1, head_pos[1])
#             if not is_adjacent(head_pos, tail_pos):
#                 tail_pos = (head_pos[0]+1, head_pos[1])
#                 tail_visited.add(tail_pos)
#
#     if direction == "R":
#         for i in range(moves_num):
#             head_pos = (head_pos[0]+1, head_pos[1])
#             if not is_adjacent(head_pos, tail_pos):
#                 tail_pos = (head_pos[0]-1, head_pos[1])
#                 tail_visited.add(tail_pos)
#
# print(len(tail_visited))

knots_pos = [(0, 0) for _ in range(10)]
tail_visited = set()
tail_visited.add((0, 0))
moves = {"L": (1, 0), "R": (-1, 0), "U": (0, -1), "D": (0, 1)}
moves_head = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

def add_tuple(left, right):
    return (left[0] + right[0], left[1]+right[1])

def is_adjacent(head, tail):
    return tail[0] in range(head[0]-1, head[0]+2) and tail[1] in range(head[1]-1, head[1]+2)

def calculate_move(head, tail):
    first = (head[0]-tail[0])
    second = (head[1]-tail[1])
    if first != 0:
        first = first // abs(first)
    if second != 0:
        second = second // abs(second)
    return (first, second)

for line in lines:
    direction, moves_num = line.split(" ")
    moves_num = int(moves_num)
    for i in range(moves_num):
        last_move = direction
        knots_pos[0] = add_tuple(knots_pos[0], moves_head[last_move])
        for knot_num in range(1, 10):
            if not is_adjacent(knots_pos[knot_num-1], knots_pos[knot_num]):
                knots_pos[knot_num] = add_tuple(knots_pos[knot_num], calculate_move(knots_pos[knot_num-1], knots_pos[knot_num]))

        tail_visited.add(knots_pos[9])

print(len(tail_visited))
