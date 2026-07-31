def solution(n):
    dp = [0]*(n+1)
    for k in range(1, n+1):
        dp[k] = dp[k-1] + k
    
    dx = [1,0,-1]
    dy = [0,1,-1]
    i = 0
    
    x, y = 0, 0
    arr = [[0]* n for _ in range(n)]
    
    num = 1
    while num <= dp[n]:
        arr[x][y] = num
        
        nx, ny = x + dx[i], y + dy[i]
        if not (0<=nx<n and 0<=ny<n) or arr[nx][ny] != 0:
            i = (i+1) % 3
            nx, ny = x + dx[i], y + dy[i]
        
        x, y = nx, ny
        num += 1
    
    answer = []
    for a in range(n):
        for b in range(n):
            if arr[a][b] != 0:
                answer.append(arr[a][b])
    return answer