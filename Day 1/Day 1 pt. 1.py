lists = open("Lists", "r")
first_list = []
second_list = []
for line in lists:
    first, second = line.strip().split()
    first_list.append(int(first))
    second_list.append(int(second))
first_list.sort()
second_list.sort()

total = 0
for i in range(0, len(first_list)):
    total += abs(first_list[i] - second_list[i])
print(total)
