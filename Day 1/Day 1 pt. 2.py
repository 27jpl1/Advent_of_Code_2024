lists = open("Lists", "r")
first_list = []
second_list = {}
for line in lists:
    first, second = line.strip().split()
    first_list.append(int(first))
    if second in second_list.keys():
        second_list[second] += 1
    else:
        second_list[second] = 1

print(second_list)
total = 0
for i in range(0, len(first_list)):
    if str(first_list[i]) in second_list.keys():
        total += first_list[i] * second_list[str(first_list[i])]
print(total)
