file = open("File", "r")

dmap = ""
for line in file:
    dmap = line.strip()
disk_map = []
for char in dmap:
    disk_map.append(int(char))
front_pointer = -1  # Starts at negative 1 because I check if space left and if not then add one
front_id = 0
back_pointer = len(disk_map) - 1
back_id = back_pointer // 2
space_left = 0
files_left = disk_map[back_pointer]
position = 0
total = 0
while front_pointer < back_pointer:
    if space_left > 0:
        if files_left > 0:
            total += position * back_id
            files_left -= 1
            space_left -= 1
            position += 1
        else:
            back_pointer -= 2
            back_id = back_pointer // 2
            files_left = disk_map[back_pointer]
    else:
        front_pointer += 1  # Move to next element which will be a set of files
        front_id = front_pointer // 2
        if front_pointer < back_pointer:
            for i in range(0, disk_map[front_pointer]):  # Add the files to the count
                total += position * front_id
                position += 1
            front_pointer += 1  # Move to the next element which is a set of free space
            space_left = disk_map[front_pointer]
        else:
            for i in range(0, files_left):
                total += position * back_id
                position += 1

print(total)



