N = int(input())
maze = list(map(int, input().split()))
dp = [float('inf')] * N 
dp[0] = 0 

for i in range(N): 
    for j in range(1, maze[i] + 1): 
        if i + j < N:
            dp[i + j] = min(dp[i + j], dp[i] + 1) # [0, 1, 2, 2, 3, 4, 4, 4, 5, 5] 가 나오게

if dp[N - 1] != float('inf'):
    print(dp[N - 1])
else:
    print(-1)