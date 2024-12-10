file = open("File", "r")

row = ""
for line in file:
    row = line.strip()

disk = []
file_id = 0

i = 0
for char in row:
    x = int(char)
    if i % 2 == 0:
        disk += [file_id] * x
        file_id += 1
    else:
        disk += [-1] * x
    i += 1

blanks = []
i = 0
for x in disk:
    if x == -1:
        blanks.append(i)
    i += 1

for blank in blanks:
    while disk[-1] == -1:
        disk.pop()
    if len(disk) <= blank:
        break
    disk[blank] = disk.pop()

total = 0
i = 0
for file in disk:
    total += i * file
    i += 1

print(total)
