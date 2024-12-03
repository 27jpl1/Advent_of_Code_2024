memory = open("Memory", "r")
lst = []
total = 0
for line in memory:
    lst.append(line.strip())
do = True
for i in range(0, len(lst)):
    for j in range(0, len(lst[i])):
        if lst[i][j] == "d":  #A possible do or dont
            if lst[i][j + 1] == "o":
                if lst[i][j + 2] == "(":
                    if lst[i][j + 3] == ")":
                        do = True
                elif lst[i][j + 2] == "n":
                    if lst[i][j + 3] == "'":
                        if lst[i][j + 4] == "t":
                            if lst[i][j + 5] == "(":
                                if lst[i][j + 6] == ")":
                                    do = False
        elif do:
            num1 = ""
            num2 = ""
            if lst[i][j] == "m":  #The start of an operation
                if lst[i][j + 1] == "u":
                    if lst[i][j + 2] == "l":
                        if lst[i][j + 3] == "(":
                            if lst[i][j + 4].isdigit():
                                k = j + 4
                                while lst[i][k].isdigit():
                                    num1 += lst[i][k]
                                    k += 1
                                if lst[i][k] == ",":
                                    if lst[i][k + 1].isdigit():
                                        l = k + 1
                                        while lst[i][l].isdigit():
                                            num2 += lst[i][l]
                                            l += 1
                                        if lst[i][l] == ")":
                                            total += int(num1) * int(num2)

print(total)
