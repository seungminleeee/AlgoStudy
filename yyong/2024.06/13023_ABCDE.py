def pado(depth, person):  # 파도깊이, 사람번호
    global result

    if depth == 5:
        print(1)
        exit(0)

    for next_person in adjl[person]:
        if not visited[next_person]:
            visited[next_person] = 1
            pado(depth + 1, next_person)
            visited[next_person] = 0   # 원상복구 필수.....

N, M = map(int, input().split())  # 사람수, 관계수
adjl = [[] for _ in range(N)]

for _ in range(M):
    p1, p2 = map(int, input().split())
    adjl[p1].append(p2)
    adjl[p2].append(p1)

for i in range(N):
    visited = [0] * N
    visited[i] = 1
    pado(1, i)

print(0)