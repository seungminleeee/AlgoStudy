def dfs(idx, lst):
    global result
    if idx == N:
        total = 0
        for i in range(N - 1):
            total += abs(lst[i] - lst[i + 1])
        result = max(result, total)
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(idx + 1, lst + [num[i]])
            visited[i] = 0
 

N = int(input())
num = list(map(int, input().split()))
visited = [0] * (N + 1)
result = 0
dfs(0, [])
print(result)

from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
per = list(permutations(num, N))

result = 0
for i in per:
    total = 0
    for j in range(N - 1):
        total += (abs(i[j] - i[j + 1]))
    result = max(result, total)

print(result)


# N = int(input())
# num = list(map(int, input().split()))
# num.sort()
# small = num[:len(num)//2]
# large = num[len(num)//2:]
# result = []
# for i in range(len(small)):
#     result.append(large[i])
#     result.append(small[i])
# if len(large) > len(small):
#     result.append(large[-1])

# cnt = 0
# for i in range(N - 1):
#     cnt += abs(result[i] - result[i + 1])

# print(cnt)