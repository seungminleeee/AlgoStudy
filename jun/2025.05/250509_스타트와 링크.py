"""
[BOJ] 스타트와 링크 / 실버1
"""
import sys
input = sys.stdin.readline

def recur(cnt, idx):
    global answer

    if cnt == N//2:
        start = 0
        link = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                elif not visited[i] and not visited[j]:
                    link += S[i][j]

        answer = min(answer, abs(start-link))

    else:
        for i in range(idx, N):
            if not visited[i]:
                visited[i] = True
                recur(cnt + 1, i)
                visited[i] = False


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N

answer = 1e9
recur(0, 0)
print(answer)