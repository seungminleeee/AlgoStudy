from collections import deque

N, M = map(int, input().split())  # 사람수, 관계수

adjl = [[] for _ in range(N+1)]

for _ in range(M):
    p1, p2 = map(int, input().split())
    adjl[p1].append(p2)
    adjl[p2].append(p1)

min_kevinbacon = 999999999999
min_kevinbacon_person = 0

for p in range(1, N+1):  # 1번부터 N번까지 너비우선탐색

    visited = [-1] * (N+1)
    visited[p] = 0
    Q = deque([p])  # rjfl

    while Q:
        cur = Q.popleft()
        
        for next in adjl[cur]:
            if visited[next] == -1:
                visited[next] = visited[cur] + 1
                Q.append(next)

    # 케빈베이컨 최솟값 확인
    kevinbacon = sum(visited) + 1

    if min_kevinbacon > kevinbacon:
        min_kevinbacon = kevinbacon
        min_kevinbacon_person = p

    elif min_kevinbacon == kevinbacon:
        if min_kevinbacon_person > p:
            min_kevinbacon_person = p

print(min_kevinbacon_person)