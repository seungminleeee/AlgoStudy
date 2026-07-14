import math

K = int(input())

power = math.ceil(math.log2(K))
area = 2 ** power

cnt = 0
if area != K:
    choco = area
    while K > 0:
        if choco > K:
            choco //= 2
            cnt += 1
        else:
            K -= choco

print(area, cnt)