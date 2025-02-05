import math

# 조약돌 종류
M = int(input())

# 각 조약돌 개수
stone = list(map(int, input().split()))

# 뽑는 조약돌 개수
K = int(input())

cases = 0
cnt = sum(stone)
for i in range(M):
    if stone[i] >= K:
        case = math.comb(stone[i], K)
        cases += case

all = math.comb(cnt, K)

ans = cases / all

print(ans)