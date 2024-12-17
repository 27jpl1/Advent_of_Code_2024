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

instruction_pointer = 0
output = ""
while instruction_pointer < len(program):
    combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C}
    jumped = False
    opcode = int(program[instruction_pointer])
    operand = int(program[instruction_pointer + 1])
    if opcode == 0:
        num = A
        denom = 2**(combo_operands[operand])
        A = num // denom
    elif opcode == 1:
        B = B ^ operand
    elif opcode == 2:
        B = combo_operands[operand] % 8
    elif opcode == 3:
        if A == 0:
            pass
        else:
            instruction_pointer = operand
            jumped = True
    elif opcode == 4:
        B = B ^ C
    elif opcode == 5:
        val = combo_operands[operand] % 8
        if len(output) == 0:
            output += str(val)
        else:
            output += "," + str(val)
    elif opcode == 6:
        num = A
        denom = 2**(combo_operands[operand])
        B = num // denom
    elif opcode == 7:
        num = A
        denom = 2**(combo_operands[operand])
        C = num // denom
    else:
        print("Opcode not expected: ", opcode)
        break
    if not jumped:
        instruction_pointer += 2

print(output)
