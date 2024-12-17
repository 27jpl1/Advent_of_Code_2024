computer = open("Computer", "r")

program = []
A = 0
B = 0
C = 0
for i, line in enumerate(computer):
    line = line.strip().split()
    if i == 0:
        A = int(line[-1])
    elif i == 1:
        B = int(line[-1])
    elif i == 2:
        C = int(line[-1])
    elif i == 3:
        pass
    else:
        program = line[-1].split(",")

for i in range(0, len(program)):
    program[i] = int(program[i])


def find(prog, ans):
    if not prog:
        return ans
    for t in range(0, 8):
        a = (ans << 3) + t
        b = a % 8
        b = b ^ 1
        c = a >> b
        b = b ^ 4
        b = b ^ c
        if b % 8 == prog[-1]:
            sub = find(prog[:-1], a)
            if sub is None:
                continue
            return sub


print(find(program, 0))
