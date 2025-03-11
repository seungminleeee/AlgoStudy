N, M = map(int, input().split())
ice = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    ice[a].append(b)
    ice[b].append(a)

ans = []
for i in range(1, N+1):
    for j in range(i+1, N+1):
        if j not in ice[i]:
            for k in range(j+1, N+1):
                if k not in ice[i] and k not in ice[j]:
                    ans.append((i, j, k))
print(len(ans))