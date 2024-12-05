search = open("Word Search", "r")

word_search = []
for line in search:
    word_search.append(line.strip())

total = 0
for i in range(0, len(word_search)):
    for j in range(0, len(word_search[i])):
        if word_search[i][j] == "S":
            if j <= len(word_search[i]) - 4 and word_search[i][j + 1] == "A":  #Striaght Right
                if word_search[i][j + 2] == "M":
                    if word_search[i][j + 3] == "X":
                        total += 1
            if j <= len(word_search[i]) - 4 and i >= 3 and word_search[i - 1][j + 1] == "A":  #Up Right
                if word_search[i - 2][j + 2] == "M":
                    if word_search[i - 3][j + 3] == "X":
                        total += 1
            if j <= len(word_search[i]) - 4 and i <= len(word_search) - 4 and word_search[i + 1][j + 1] == "A":  #Down Right
                if word_search[i + 2][j + 2] == "M":
                    if word_search[i + 3][j + 3] == "X":
                        total += 1
            if i <= len(word_search) - 4 and word_search[i + 1][j] == "A":  #Straight Down
                if word_search[i + 2][j] == "M":
                    if word_search[i + 3][j] == "X":
                        total += 1
        elif word_search[i][j] == "X":
            if j <= len(word_search[i]) - 4 and word_search[i][j + 1] == "M":  #Straight Right
                if word_search[i][j + 2] == "A":
                    if word_search[i][j + 3] == "S":
                        total += 1
            if j <= len(word_search[i]) - 4 and i >= 3 and word_search[i - 1][j + 1] == "M":  #Up Right
                if word_search[i - 2][j + 2] == "A":
                    if word_search[i - 3][j + 3] == "S":
                        total += 1
            if j <= len(word_search[i]) - 4 and i <= len(word_search) - 4 and word_search[i + 1][j + 1] == "M":  #Down Right
                if word_search[i + 2][j + 2] == "A":
                    if word_search[i + 3][j + 3] == "S":
                        total += 1
            if i <= len(word_search) - 4 and word_search[i + 1][j] == "M":  #Straight Right
                if word_search[i + 2][j] == "A":
                    if word_search[i + 3][j] == "S":
                        total += 1
print(total)
