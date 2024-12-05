search = open("Word Search", "r")

word_search = []
for line in search:
    word_search.append(line.strip())

total = 0
for i in range(0, len(word_search)):
    for j in range(0, len(word_search[i])):
        if word_search[i][j] == "A" and 0 < i < len(word_search) - 1 and 0 < j < len(word_search[i]) - 1:
            if word_search[i - 1][j - 1] == "M" and word_search[i - 1][j + 1] == "M":  #M's on top
                if word_search[i + 1][j - 1] == "S" and word_search[i + 1][j + 1] == "S":
                    total += 1
            if word_search[i + 1][j - 1] == "M" and word_search[i + 1][j + 1] == "M":  #M's on bottom
                if word_search[i - 1][j - 1] == "S" and word_search[i - 1][j + 1] == "S":
                    total += 1
            if word_search[i - 1][j - 1] == "M" and word_search[i + 1][j - 1] == "M":  #M's on left
                if word_search[i - 1][j + 1] == "S" and word_search[i + 1][j + 1] == "S":
                    total += 1
            if word_search[i - 1][j + 1] == "M" and word_search[i + 1][j + 1] == "M":  #M's on right
                if word_search[i - 1][j - 1] == "S" and word_search[i + 1][j - 1] == "S":
                    total += 1

print(total)
