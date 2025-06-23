def solution(n, computers):
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    
    cnt = 0
    visited = [0]*n
    def bfs(v):
        q = [v]
        visited[v] = 1
        
        while q:
            curr = q.pop(0)
            
            for next in graph[curr]:
                if visited[next] == 0:
                    q.append(next)
                    visited[next] = 1
            
    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            cnt += 1
            
    return cnt