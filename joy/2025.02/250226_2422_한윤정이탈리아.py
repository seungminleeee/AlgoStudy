from itertools import combinations

N, M = map(int, input().split())
ice_cream = [i for i in range(1, N + 1)]
ice = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    ice[x].append(y)
    ice[y].append(x)

ice_com = list(combinations(ice_cream, 3))
cnt = 0 
for i1, i2, i3 in ice_com:
    if i2 in ice[i1] or i3 in ice[i1] or i3 in ice[i2]:
        continue
    cnt += 1
print(cnt)