from collections import deque

def func(A):
    global cnt

    q = deque([(A, 0)])
    visited[A] = 1

    while q:
        cx, idx = q.popleft()

        if idx == 2:
            return

        for x in arr[cx]:
            if visited[x] == 0:
                q.append((x, idx + 1))
                visited[x] = 1
                cnt += 1

N = int(input())

arr = [[] for _ in range(N)]
for k in range(N):
    lst = list(map(str, input()))
    for l in range(N):
        if lst[l] == 'Y':
            arr[k].append(l)

ans = 0
for i in range(N):
    visited = [0]*N
    cnt = 0
    func(i)
    ans = max(ans, cnt)

print(ans)