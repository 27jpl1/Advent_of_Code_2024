reports = open("Reports", "r")
report_list = []
for line in reports:
    report_list.append(line.strip().split())

for i in range(0, len(report_list)):
    for j in range(0, len(report_list[i])):
        report_list[i][j] = int(report_list[i][j])

total = 0
for i in range(0, len(report_list)):
    level_safe = True
    if report_list[i][0] < report_list[i][1]:
        increasing = True
    else:
        increasing = False
    for j in range(0, len(report_list[i]) - 1):
        first = report_list[i][j]
        second = report_list[i][j + 1]
        if 1 <= abs(first - second) <= 3:
            if first - second > 0 and not increasing:
                pass
            elif first - second < 0 and increasing:
                pass
            else:
                level_safe = False
                j = len(report_list[i])
            # level is safe so far
        else:
            level_safe = False
            break
    if level_safe:
        total += 1
print(total)
