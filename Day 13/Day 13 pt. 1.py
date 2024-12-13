import sys

claw_machines = open("Claw Machines", "r")

cords = []
for line in claw_machines:
    line = line.strip().split()
    if len(line) == 4:
        cords.append((int(line[2][2:-1]), int(line[3][2:])))
    elif len(line) == 3:
        cords.append((int(line[1][2:-1]), int(line[2][2:])))


def run_sim(button_a, button_b, prize):
    lowest_cost = sys.maxsize
    button_a_x, button_a_y = button_a
    button_b_x, button_b_y = button_b
    prize_x, prize_y = prize
    for j in range(0, 100):  #Will represent how many times button a has been pressed
        for k in range(0, 100):  #Will represent how many times button b has been pressed
            if button_a_x * j + button_b_x * k == prize_x and button_a_y * j + button_b_y * k == prize_y:
                if lowest_cost > j * 3 + k:
                    lowest_cost = j * 3 + k
            if button_a_x * j + button_b_x * k > prize_x or button_a_y * j + button_b_y * k > prize_y:
                break
    if lowest_cost == sys.maxsize:
        return 0
    else:
        return lowest_cost


i = 0
total = 0
while i < len(cords):
    total += run_sim(cords[i], cords[i + 1], cords[i + 2])
    i += 3
print(total)
