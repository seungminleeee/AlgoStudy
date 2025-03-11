"""
[BOJ] 11404번: 플로이드 / 골드4
"""
import sys

input = sys.stdin.readline

n = int(input())  # (2 ≤ n ≤ 100)
m = int(input())  # (1 ≤ m ≤ 100,000)
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]

# 자기 자신 0 처리
for i in range(1, n + 1):
    graph[i][i] = 0

# 노드 값 넣기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

# 플로이드-워셜 (최소 비용 i, j 쌍 찾기)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] != float('inf') and graph[k][j] != float('inf'):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
for i in range(1, n + 1):
    print(' '.join(str(0 if graph[i][j] == float('inf') else graph[i][j]) for j in range(1, n + 1)))