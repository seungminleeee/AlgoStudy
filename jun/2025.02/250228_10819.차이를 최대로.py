"""
[BOJ] 10819번: 차이를 최대로 / 실버2
"""
def dfs():
    global answer

    if len(temp) == n:
        cur_sum = 0
        for i in range(n - 1):
            cur_sum += abs(temp[i] - temp[i + 1])
        answer = max(answer, cur_sum)
        return

    # 백트래킹
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            temp.append(arr[i])
            dfs()
            temp.pop()
            visited[i] = False


n = int(input())  # (3 ≤ N ≤ 8)
arr = list(map(int, input().split()))

visited = [False] * n
temp = []
answer = 0

dfs()
print(answer)