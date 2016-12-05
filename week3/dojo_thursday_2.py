import random

coordsys = []

for x in range(0, 5):
    coordsys.append([])
    for y in range(0, 5):
        coordsys[x].append(0)
coordsys[2][2] = "X"
middle_x = 2
middle_y = 2
robot_snail_pos_x = random.randint(0, 5)
robot_snail_pos_y = random.randint(0, 5)
robot_snail_pos = coordsys[robot_snail_pos_x][robot_snail_pos_y]
coordsys[robot_snail_pos_x][robot_snail_pos_y] = "S"
print(coordsys)
if robot_snail_pos_x >= 2:
    distance_x = middle_x - robot_snail_pos_x
else:
    distance_x = robot_snail_pos_x - middle_x
if robot_snail_pos_y >= 2:
    distance_y = middle_y - robot_snail_pos_y
else:
    distance_y = robot_snail_pos_y - middle_y
print("The distance is : x: ", distance_x, "y: ", distance_y)
