res = [[0 for i in range(11)] for j in range(21)]

for i in range(21):
    for j in range(11):
        if j * 2 == i and i != 0:
            res[(20 - i) % 20][j] += 1

for i in range(21):
    line = ''
    for j in range(11):
        if j == 0:
            line += '\t' + str(20-i) + '\t'
        else:
            if res[i][j] == 0:
                line += '---'
            if res[i][j] == 1:
                line += '!!'
    print(line)
print('\t 0  1  2  3  4  5  6  7  8  9  10')
