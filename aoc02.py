with open("./inputs/aoc02.in", 'r') as fp:
    lines = fp.readlines()

score_type = {"X": 0, "Y": 3, "Z": 6}
score_match = {("A", "X"): 3, ("B", "X"): 1, ("C", "X"): 2,
               ("A", "Y"): 1, ("B", "Y"): 2, ("C", "Y"): 3,
               ("A", "Z"): 2, ("B", "Z"): 3, ("C", "Z"): 1,
               }
total_score = 0
for line in lines:
    x, y = line.strip("\n").split(" ")
    total_score += score_match[(x, y)] + score_type[y]

print(total_score)
