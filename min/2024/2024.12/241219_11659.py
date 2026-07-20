N, M = map(int, input().split())
arr = list(map(int, input().split()))

lst = [0 for _ in range(N+1)]

for j in range(N):
    lst[j+1] = lst[j] + arr[j]

for i in range(M):
    s, e = map(int, input().split())
    ans = lst[e] - lst[s-1]
    print(ans)