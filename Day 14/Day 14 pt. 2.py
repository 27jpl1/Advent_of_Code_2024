import sys

robot_list = open("Robots", "r")

robots = []
width = 101
height = 103
for line in robot_list:
    line = line.strip().split()
    robot = []
    for part in line:
        part = part.split(",")
        robot.append(int(part[0][2:]))
        robot.append(int(part[1]))
    robots.append(robot)


def run_robot(x_pos, y_pos, x_vel, y_vel):
    if x_pos + x_vel >= width:  #>= since indexing at 0
        x_pos = 0 + abs(width - x_pos - x_vel)
    elif x_pos + x_vel < 0:  #Assumes x_vel is neg
        x_pos = width + x_vel + x_pos
    else:
        x_pos += x_vel
    if y_pos + y_vel >= height:  #>= since indexing at 0
        y_pos = 0 + abs(height - y_pos - y_vel)
    elif y_pos + y_vel < 0:  #Assumes y_vel is neg
        y_pos = height + y_vel + y_pos
    else:
        y_pos += y_vel

    return x_pos, y_pos


for i in range(width * height):
    robots_pos = set()
    same_spot = False
    for j in range(0, len(robots)):
        x, y = run_robot(robots[j][0], robots[j][1], robots[j][2], robots[j][3])
        robots[j][0], robots[j][1] = x, y
        if same_spot:
            pass
        else:
            if (x, y) in robots_pos:
                same_spot = True
            else:
                robots_pos.add((x,y))
    if not same_spot:
        print(i + 1)



