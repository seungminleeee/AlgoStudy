"""
[BOJ] 점프 점프 / 실버2
"""
from collections import deque

def bfs(start):
    visited = [False] * n
    visited[start] = True
    queue = deque([(start, 0)])

    while queue:
        cur_pos, jump_count = queue.popleft()

        if cur_pos == n - 1:
            return jump_count

        for next_pos in range(cur_pos + 1, cur_pos + A[cur_pos] + 1):
            if next_pos < n and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, jump_count + 1))

    return -1

n = int(input())  # (1 ≤ N ≤ 1,000)
A = list(map(int, input().split()))

print(bfs(0))