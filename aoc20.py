with open("./inputs/aoc20.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

numbers = [(int(lines[i]) * 811589153, i) for i in range(len(lines))]
cached_position = {i: i for i in range(len(lines))}
org_numbers = [int(line) for line in lines]
n = len(numbers)

def get_cached(index):
    cached_pos = cached_position[index]
    if numbers[cached_pos][1] == index:
        return cached_pos

    for i in range(1, 111):
        new_position = (n + cached_pos + i) % n
        cached_position[numbers[new_position][1]] = new_position
        if numbers[new_position][1] == index:
            return new_position

    for i in range(1, 111):
        new_position = (n + cached_pos - i) % n
        cached_position[numbers[new_position][1]] = new_position
        if numbers[new_position][1] == index:
            return new_position

    for i in range(len(numbers)):
        cached_position[numbers[i][1]] = i
        if numbers[i][1] == index:
            return i


def move_num(index):
    global n, numbers, org_numbers
    position = get_cached(index)
    num = numbers.pop(position)
    numbers.insert((position + num[0]) % (n-1), num)


for j in range(10):
    for i in range(n):
        move_num(i)

zero_pos = 0
for i in range(n):
    if numbers[i][0] == 0:
        zero_pos = i
        break

print(numbers[(zero_pos + 1000) % n][0] + numbers[(zero_pos + 2000) % n][0] + numbers[(zero_pos + 3000) % n][0])
