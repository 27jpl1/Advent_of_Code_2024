manual = open("Manual", "r")

in_ordering = True
orders = {}
updates = []
i = 0
for line in manual:
    line = line.strip()
    if line == "":
        in_ordering = False
    elif in_ordering:
        if line[0:2] in orders.keys():
            orders[line[0:2]].append(line[3:5])
        else:
            orders[line[0:2]] = [line[3:5]]
    else:
        j = 0
        updates.append([])
        while j < len(line) - 1:
            updates[i].append(line[j: j + 2])
            j += 3
        i += 1
print(orders)
total = 0
for k in range(0, len(updates)):
    failed = False
    l = len(updates[k]) - 1
    while l >= 0:
        for m in range(0, l):
            if updates[k][l] in orders.keys():
                if updates[k][m] in orders[updates[k][l]]:
                    failed = True
                    temp = updates[k].pop(l)
                    updates[k].insert(m, temp)
        l -= 1
    if failed:
        middle = len(updates[k])//2
        total += int(updates[k][middle])
print(total)
