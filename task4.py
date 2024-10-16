END = '\u001b[0m'
SET_COLOR = "\x1b[48;5;"

f = [float(i) for i in open('sequence')]

cnt0, cnt1 = 0, 0
for i in range(len(f)):
    if i % 2 == 0:
        cnt0 += abs(f[i])
    else:
        cnt1 += abs(f[i])

cnt0, cnt1 = round(cnt0 // 10), round(cnt1 // 10)

print(f"сум чисел на четных позициях: {SET_COLOR}10m{' '*cnt0}{END}")
print(f"сум чисел на нечетн позициях: {SET_COLOR}18m{' '*cnt1}{END}")
