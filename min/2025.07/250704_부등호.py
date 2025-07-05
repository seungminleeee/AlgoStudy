import sys;sys.stdin=open('input.txt')

def dfs(k, st):
    global ans
    if k == N:
        ans.append(st)
        return

    for i in range(10):
        if visited[i] == 0:
            if k == -1 or (sign[k] == '<' and st[-1] < str(i)) or (sign[k] == '>' and st[-1] > str(i)):
                visited[i] = 1
                dfs(k+1, st + str(i))
                visited[i] = 0

N = int(input())
sign = list(input().split())

visited = [0]*10
ans = []
dfs(-1, "")

print(max(ans))
print(min(ans))