N, M = map(int, input().split())
arr = []

for i in range(N):
    energy = list(map(int, input().split()))
    arr.append(energy)

min_energy = 999999999999

def dfs(x, y, prev, total_energy):
    global min_energy

    if x == N:
        min_energy = min(min_energy, total_energy)
        return
    
    for direc in range(-1, 2):
        if direc == prev:
            continue
        
        nx, ny = x + 1, y + direc
        if 0 <= ny < M :
            dfs(nx, ny, direc, total_energy + arr[x][y])
    
for j in range(M):
    dfs(0, j, None, 0)

print(min_energy)