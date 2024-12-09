file = open("File", "r")

row = ""
for line in file:
    row = line.strip()

file_id = 0
files = {}
blanks = []
position = 0

i = 0
for char in row:
    x = int(char)
    if i % 2 == 0:
        files[file_id] = (position, x)
        file_id += 1
    else:
        if x != 0:
            blanks.append((position, x))
    position += x
    i += 1

while file_id > 0:
    file_id -= 1
    position, size = files[file_id]
    i = 0
    for blank in blanks:
        start, length = blank
        if start >= position:
            blanks = blanks[:i]
            break
        if size <= length:
            files[file_id] = (start, size)
            if size == length:
                blanks.pop(i)
            else:
                blanks[i] = (start + size, length - size)
            break
        i += 1

total = 0
for file in files.items():
    id, (pos, size) = file
    for i in range(pos, pos + size):
        total += id * i

print(total)

