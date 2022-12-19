import sys

with open("./inputs/aoc15.in", 'r') as fp:
    lines = fp.readlines()
    lines = [line.strip("\n") for line in lines]

sensor_to_beacon = {}
all_sensors = []
all_beacons = []
sensor_to_beacon_dist = {}

def manhattan(first, second):
    return abs(first[0] - second[0]) + abs(first[1]-second[1])

min_x = sys.maxsize
max_x = 0
for line in lines:
    splitted = line.split()
    sensor_x = int(splitted[2].strip(',').split('=')[1])
    sensor_y = int(splitted[3].strip(':').split('=')[1])
    beacon_x = int(splitted[-2].strip(',').split('=')[1])
    beacon_y = int(splitted[-1].strip(':').split('=')[1])
    min_x = min(sensor_x, min_x)
    max_x = max(sensor_x, max_x)
    sensor_to_beacon[(sensor_x, sensor_y)] = (beacon_x, beacon_y)
    all_sensors.append((sensor_x, sensor_y))
    all_beacons.append((beacon_x, beacon_y))
    sensor_to_beacon_dist[(sensor_x, sensor_y)] = manhattan((sensor_x, sensor_y), (beacon_x, beacon_y))

maximum_distance = max(sensor_to_beacon_dist.values())
out = 0
set_y = 2000000
# for i in range(min_x - maximum_distance - 10, max_x + maximum_distance + 10):
#     new_sensors = []
#     for sensor in all_sensors:
#         if manhattan(sensor, (i, set_y)) <= sensor_to_beacon_dist[sensor]:
#             if (i, set_y) not in all_beacons:
#                 out += 1
#             break
#         # else:
#         #     if i <= sensor[0]:
#         #         new_sensors.append(sensor)
#     else:
#         #all_sensors = new_sensors
#         continue
#
#     #all_sensors = new_sensors
#
# print(out)

set_start = 0
set_stop = 4000000
breaked = False
i = set_start
j = set_start
while i < set_stop:
    j = set_start
    while j < set_stop:
        breaked = False
        for sensor in all_sensors:
            dist = manhattan(sensor, (j, i))
            if manhattan(sensor, (j, i)) <= sensor_to_beacon_dist[sensor]:
                if sensor_to_beacon_dist[sensor] == dist:
                    j += 1
                else:
                    j += (sensor_to_beacon_dist[sensor] - dist)
                breaked = True
                break

        if breaked:
            continue

        print(j * 4000000 + i)
        j += 1
    i += 1
