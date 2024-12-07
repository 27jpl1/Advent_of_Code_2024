lst = open("Repairs", "r")

repairs = []
for line in lst:
    repair = []
    line = line.strip()
    seen_colon = False
    value = ""
    for char in line:
        if not seen_colon:
            if char == ":":
                repair.append(int(value))
                value = ""
                seen_colon = True
            else:
                value += char
        else:
            if char == " " and value != "":
                repair.append(int(value))
                value = char
            else:
                value += char
    repair.append(int(value))
    repairs.append(repair)


def run_sim(operations, repair):
    total = repair[0]
    value = 0
    if operations[0] == "+":
        value = repair[1] + repair[2]
    else:
        value = repair[1] * repair[2]
    i = 1
    while i < len(operations):
        if operations[i] == "+":
            value += repair[i + 2]
        else:
            value *= repair[i + 2]
        i += 1
    return total == value


total = 0
for repair in repairs:
    test_value = repair[0]
    size = len(repair) - 2  #Minus for the first elements and minus because need n - 1 operations for n elements
    operations = ["+"] * size
    works = run_sim(operations, repair)
    if works:
        total += test_value
    else:
        for i in range(0, 2**size - 1):
            flipped_to_mult = False
            op = 0
            while not flipped_to_mult:
                if operations[op] == "+":
                    operations[op] = "*"
                    flipped_to_mult = True
                else:
                    operations[op] = "+"
                op += 1
            works = run_sim(operations, repair)
            if works:
                total += test_value
                break
print(total)
