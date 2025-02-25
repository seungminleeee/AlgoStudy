"""
[BOJ] 2617번: 구슬 찾기 / 골드4
"""
n, m = map(int, input().split())  # 1 <= n <= 99,  1 <= m <= n(n-1)/2

# 인접 리스트 생성
heavier = [[] for _ in range(n + 1)]
lighter = [[] for _ in range(n + 1)]

# 노드 연결
for _ in range(m):
    heavy_bead, light_bead = map(int, input().split())
    heavier[heavy_bead].append(light_bead)
    lighter[light_bead].append(heavy_bead)

# 구슬 카운트
def dfs(graph, start, visited):
    count = 0
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            count += 1 + dfs(graph, next, visited)
    return count

answer = 0
mid = (n + 1) // 2
for i in range(1, n + 1):
    # 무거운 구슬 카운트
    heavy_visited = [False] * (n + 1)
    heavy_count = dfs(heavier, i, heavy_visited)
    # 가벼운 구슬 카운트
    light_visited = [False] * (n + 1)
    light_count = dfs(lighter, i, light_visited)
    # 중간인 구슬이 될 수 없는 구슬 카운트
    if heavy_count >= mid or light_count >= mid:
        answer += 1

print(answer)