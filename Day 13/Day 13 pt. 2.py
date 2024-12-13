import sympy

claw_machines = open("Claw Machines", "r")

cords = []
for line in claw_machines:
    line = line.strip().split()
    if len(line) == 4:
        cords.append((int(line[2][2:-1]), int(line[3][2:])))
    elif len(line) == 3:
        cords.append((int(line[1][2:-1]), int(line[2][2:])))


def run_sim(button_a, button_b, prize):
    button_a_x, button_a_y = button_a
    button_b_x, button_b_y = button_b
    prize_x, prize_y = prize
    prize_x = prize_x + 10000000000000
    prize_y = prize_y + 10000000000000
    j, k = sympy.sympify("j, k")  #j is the # of times button a is pushed and k is the same for button b
    answers = sympy.solve([prize_x - (button_a_x * j) - (button_b_x * k), prize_y - (button_a_y * j) - (button_b_y * k)])
    if not answers:
        return 0
    else:
        j = float(answers[j])
        k = float(answers[k])
        if j.is_integer() and k.is_integer():
            return j * 3 + k
        else:
            return 0


i = 0
total = 0
while i < len(cords):
    total += run_sim(cords[i], cords[i + 1], cords[i + 2])
    i += 3
print(int(total))

