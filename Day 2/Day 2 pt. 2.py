reports = open("Reports", "r")
report_list = []
for line in reports:
    report_list.append(line.strip().split())

for i in range(0, len(report_list)):
    for j in range(0, len(report_list[i])):
        report_list[i][j] = int(report_list[i][j])


def check_lists(lst):
    num_safe = 0
    for i in range(0, len(lst)):
        level_safe = True
        if lst[i][0] < lst[i][1]:
            increasing = True
        else:
            increasing = False
        for j in range(0, len(lst[i]) - 1):
            first = lst[i][j]
            second = lst[i][j + 1]
            if 1 <= abs(first - second) <= 3:
                if first - second > 0 and not increasing:
                    pass
                elif first - second < 0 and increasing:
                    pass
                else:
                    level_safe = False
            else:
                level_safe = False
                break
        if level_safe:
            num_safe += 1
    if num_safe > 0:
        return True
    else:
        return False


total = 0
for i in range(0, len(report_list)):
    sets = []
    for j in range(0, len(report_list[i])):
        taken = report_list[i].pop(j)
        new_lst = report_list[i].copy()
        sets.append(new_lst)
        report_list[i].insert(j, taken)
    if check_lists(sets):
        total += 1
print(total)
