m = open("Map", "r")

og_map = []
start_pos = ()
i = 0
for line in m:
    line = line.strip()
    if "^" in line:
        start_pos = (i, line.index("^"))
    og_map.append(line.strip())
    i += 1


def check_loop(map, pos):
    loop = False
    out = False
    seen = set()
    current_char = "^"
    while not out and not loop:
        if current_char == "^":
            if pos[0] - 1 == -1:
                out = True
            elif map[pos[0] - 1][pos[1]] == "#":
                current_char = ">"
            else:
                if (pos, current_char) not in seen:
                    seen.add((pos, current_char))
                else:
                    loop = True
                pos = (pos[0] - 1, pos[1])
        elif current_char == ">":
            if pos[1] + 1 == len(map[0]):
                out = True
            elif map[pos[0]][pos[1] + 1] == "#":
                current_char = "v"
            else:
                if (pos, current_char) not in seen:
                    seen.add((pos, current_char))
                else:
                    loop = True
                pos = (pos[0], pos[1] + 1)
        elif current_char == "<":
            if pos[1] - 1 == -1:
                out = True
            elif map[pos[0]][pos[1] - 1] == "#":
                current_char = "^"
            else:
                if (pos, current_char) not in seen:
                    seen.add((pos, current_char))
                else:
                    loop = True
                pos = (pos[0], pos[1] - 1)
        else:
            if pos[0] + 1 == len(map):
                out = True
            elif map[pos[0] + 1][pos[1]] == "#":
                current_char = "<"
            else:
                if (pos, current_char) not in seen:
                    seen.add((pos, current_char))
                pos = (pos[0] + 1, pos[1])
    return loop


total = 0
j = 0
while j < len(og_map):
    print(j)
    k = 0
    while k < len(og_map[j]):
        new_map = og_map.copy()
        if new_map[j][k] == ".":
            new_map[j] = new_map[j][0:k] + "#" + new_map[j][k + 1:]
        if check_loop(new_map, start_pos):
            total += 1
        k += 1
    j += 1

print(total)
