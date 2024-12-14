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
    for i in range(0, 100):
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


quad_0 = 0  #Count of robots in top left
quad_1 = 0  #Count of robots in top right
quad_2 = 0  #Count of robots in bottom left
quad_3 = 0  #Count of robot in bottom right
for robot in robots:
    x, y = run_robot(robot[0], robot[1], robot[2], robot[3])
    if x < (width - 1) / 2 and y < (height - 1) / 2:
        quad_0 += 1
    elif x > (width - 1) / 2 and y < (height - 1) / 2:
        quad_1 += 1
    elif x < (width - 1) / 2 and y > (height - 1) / 2:
        quad_2 += 1
    elif x > (width - 1) / 2 and y > (height - 1) / 2:
        quad_3 += 1
print(quad_0 * quad_1 * quad_2 * quad_3)


