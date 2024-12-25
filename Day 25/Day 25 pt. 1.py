file = open("Keys", "r")

keys = []
locks = []

heights = [0, 0, 0, 0, 0]
start = True
for line in file:
    line = line.strip()
    if start:
        start = False
        if line[0] == "#":
            is_key = False
            for i, char in enumerate(line):
                if char == "#":
                    heights[i] += 1
        else:
            is_key = True
    elif line == "":
        start = True
        if is_key:
            keys.append(heights)
        else:
            locks.append(heights)
        heights = [0, 0, 0, 0, 0]
    else:
        for i, char in enumerate(line):
            if char == "#":
                heights[i] += 1
if is_key:
    keys.append(heights)
else:
    locks.append(heights)

total = 0
for lock in locks:
    for key in keys:
        fits = True
        for i in range(0, 5):
            if lock[i] + key[i] > 7:
                fits = False
        if fits:
            total += 1
            print(lock, key)
print(total)
