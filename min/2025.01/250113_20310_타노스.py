S = list(map(int, input()))
cnt_1 = S.count(1) // 2
cnt_0 = S.count(0) // 2

check_1 = 0
for s in S:
    if check_1 == cnt_1:
        break
    if s == 1:
        check_1 += 1
        S.remove(s)

check_0 = 0
S = S[::-1]
for s in S:
    if check_0 == cnt_0:
        break
    if s == 0:
        check_0 += 1
        S.remove(s)


print("".join(map(str,S[::-1])))