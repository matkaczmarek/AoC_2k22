import functools


with open("inputs/aoc11.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

monkey_items = {}
monkey_mult = {}
monkey_div = {}
monkey_op = {}
monkey_true = {}
monkey_false = {}
monkey_count = {}
i = 0
item_counter = 0

while i < len(lines):
    monkey_num = int(lines[i].split(" ")[-1].strip(":"))
    monkey_count[monkey_num] = 0
    items = lines[i+1].split(" ")[4:]
    items = [int(it.strip(",")) for it in items]
    monkey_items[monkey_num] = items
    operation = lines[i+2].split(" ")
    monkey_op[monkey_num] = operation[-2]
    mult = operation[-1]
    monkey_mult[monkey_num] = mult
    div = int(lines[i+3].split(" ")[-1])
    monkey_div[monkey_num] = div
    true = int(lines[i+4].split(" ")[-1])
    monkey_true[monkey_num] = true
    false = int(lines[i+5].split(" ")[-1])
    monkey_false[monkey_num] = false
    i += 7

combined_mul = functools.reduce(lambda x, y: x * y, monkey_div.values())

# for i in range(20):
#     for num in monkey_items.keys():
#         for item in monkey_items[num]:
#             monkey_count[num] += 1
#             if monkey_op[num] == "*":
#                 if monkey_mult[num] == "old":
#                     item = item * item
#                 else:
#                     item *= int(monkey_mult[num])
#             else:
#                 if monkey_mult[num] == "old":
#                     item = item + item
#                 else:
#                     item += int(monkey_mult[num])
#             item //= 3
#             if item % monkey_div[num] == 0:
#                 monkey_items[monkey_true[num]].append(item)
#             else:
#                 monkey_items[monkey_false[num]].append(item)
#         monkey_items[num] = []
#
#
# sorted_monkeys = sorted(monkey_count.values(), reverse=True)
# print(sorted_monkeys[0] * sorted_monkeys[1])


for i in range(10000):
    for num in monkey_items.keys():
        for item in monkey_items[num]:
            monkey_count[num] += 1
            if monkey_op[num] == "*":
                if monkey_mult[num] == "old":
                    item = (item * item) % combined_mul
                else:
                    item = (item*int(monkey_mult[num])) % combined_mul
            else:
                if monkey_mult[num] == "old":
                    item = (item + item) % combined_mul
                else:
                    item = (item + int(monkey_mult[num])) % combined_mul
            # item //= 3
            if item % monkey_div[num] == 0:
                monkey_items[monkey_true[num]].append(item)
            else:
                monkey_items[monkey_false[num]].append(item)
        monkey_items[num] = []

sorted_monkeys = sorted(monkey_count.values(), reverse=True)
print(sorted_monkeys[0] * sorted_monkeys[1])