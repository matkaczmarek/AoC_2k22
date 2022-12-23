with open("./inputs/aoc23.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

elves_pos = []
position_taken = set()
is_elf_moving = []
proposed_moves_ctr = {}
proposed_moves_to_elf = {}
N = [(-1, 0), (-1, 1), (-1, -1)]
S = [(1, 0), (1, 1), (1, -1)]
W = [(0, -1), (-1, -1), (1, -1)]
E = [(0, 1), (-1, 1), (1, 1)]
directions = [N, S, W, E]


for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            elves_pos.append((i, j))
            position_taken.add((i, j))

def add_tuple(left, right):
    return (left[0] + right[0], left[1]+right[1])

def have_to_move(elf_idx):
    global elves_pos, is_elf_moving, directions, position_taken, proposed_moves_ctr, proposed_moves_to_elf
    curr_elf_pos = elves_pos[elf_idx]
    for dir in directions:
        for x in dir:
            proposed_pos = add_tuple(curr_elf_pos, x)
            if proposed_pos in position_taken:
                return True

    return False

def propose_move(elf_idx):
    global elves_pos, is_elf_moving, directions, position_taken, proposed_moves_ctr, proposed_moves_to_elf
    curr_elf_pos = elves_pos[elf_idx]
    for dir in directions:
        can_move = True
        for x in dir:
            proposed_pos = add_tuple(curr_elf_pos, x)
            if proposed_pos in position_taken:
                can_move = False

        if can_move:
            proposed_pos = add_tuple(curr_elf_pos, dir[0])
            proposed_moves_to_elf[elf_idx] = proposed_pos
            if proposed_pos in proposed_moves_ctr.keys():
                proposed_moves_ctr[proposed_pos] += 1
            else:
                proposed_moves_ctr[proposed_pos] = 1
            break

def make_move(elf_idx):
    global elves_pos, is_elf_moving, directions, position_taken, proposed_moves_ctr, proposed_moves_to_elf
    if elf_idx not in proposed_moves_to_elf.keys():
        return

    proposed_mov = proposed_moves_to_elf[elf_idx]
    if proposed_moves_ctr[proposed_mov] > 1:
        return

    position_taken.remove(elves_pos[elf_idx])
    position_taken.add(proposed_mov)
    elves_pos[elf_idx] = proposed_mov

def clear_state():
    global elves_pos, is_elf_moving, directions, position_taken, proposed_moves_ctr, proposed_moves_to_elf
    is_elf_moving = []
    proposed_moves_ctr = {}
    proposed_moves_to_elf = {}
    dir = directions.pop(0)
    directions.append(dir)

round_ctr = 0
while any([have_to_move(idx) for idx in range(len(elves_pos))]):
    round_ctr += 1
    for idx in range(len(elves_pos)):
        if not have_to_move(idx):
            is_elf_moving.append(False)
            continue
        is_elf_moving.append(True)

        propose_move(idx)
    for idx in range(len(elves_pos)):
        if not is_elf_moving[idx]:
            continue

        make_move(idx)

    clear_state()

min_x = min(elf[0] for elf in elves_pos)
max_x = max(elf[0] for elf in elves_pos)
min_y = min(elf[1] for elf in elves_pos)
max_y = max(elf[1] for elf in elves_pos)

print(round_ctr + 1)
#print((abs(min_x - max_x) + 1) * (abs(min_y - max_y) + 1) - len(elves_pos))
