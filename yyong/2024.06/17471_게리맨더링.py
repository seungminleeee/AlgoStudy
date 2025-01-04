# 파이썬 34112 KB, 56 ms
# 파이파이 114328 KB, 136 ms

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
population = [0] + list(map(int, input().split()))
population_sum = sum(population)
adjl = [[]] + [list(map(int, input().split()))[1:] for _ in range(N)]


# 연결 노드 확인 bfs
def check(arr):

    if len(arr) == 1:
        return True

    visited = [0] * (N+1)
    lst = [arr[0]]
    Q = deque([arr[0]])
    visited[arr[0]] = 1

    while Q:
        cur = Q.popleft()

        for next in adjl[cur]:
            if not visited[next] and next in arr:
                lst.append(next)
                Q.append(next)
                visited[next] = 1

    return len(arr) == len(lst)


min_diff = float('inf')

# 조합 백트래킹
def comb(n, first, first_p):
    global min_diff

    if min_diff == 0:
        return

    if n == N:
        if len(first) == N or len(first) == 0:
            return
        
        second = []

        for a in list(range(1, N+1)):
            if a not in first:
                second.append(a)

        second_p = population_sum - first_p

        if check(first) and check(second):
            min_diff = min(abs(first_p - second_p), min_diff)

        return

    comb(n+1, first + [n], first_p + population[n])

    comb(n+1, first, first_p)

comb(1, [], 0)

if min_diff == float('inf'):
    print(-1)
else:
    print(min_diff)