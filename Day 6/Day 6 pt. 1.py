m = open("Map", "r")

map = []
pos = ()
i = 0
for line in m:
    line = line.strip()
    if "^" in line:
        pos = (i, line.index("^"))
    map.append(line.strip())
    i += 1

out = False
seen = set()
current_char = "^"
while not out:
    print(pos)
    if current_char == "^":
        if pos[0] - 1 == -1:
            out = True
        elif map[pos[0] - 1][pos[1]] == "#":
            current_char = ">"
        else:
            if pos not in seen:
                seen.add(pos)
            pos = (pos[0] - 1, pos[1])
    elif current_char == ">":
        if pos[1] + 1 == len(map[0]):
            out = True
        elif map[pos[0]][pos[1] + 1] == "#":
            current_char = "v"
        else:
            if pos not in seen:
                seen.add(pos)
            pos = (pos[0], pos[1] + 1)
    elif current_char == "<":
        if pos[1] - 1 == -1:
            out = True
        elif map[pos[0]][pos[1] - 1] == "#":
            current_char = "^"
        else:
            if pos not in seen:
                seen.add(pos)
            pos = (pos[0], pos[1] - 1)
    else:
        if pos[0] + 1 == len(map):
            out = True
        elif map[pos[0] + 1][pos[1]] == "#":
            current_char = "<"
        else:
            if pos not in seen:
                seen.add(pos)
            pos = (pos[0] + 1, pos[1])
print(len(seen) + 1)
