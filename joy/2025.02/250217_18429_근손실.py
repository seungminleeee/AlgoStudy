from itertools import permutations

N, K = map(int, input().split())
weight = list(map(int, input().split()))
result = list(permutations(weight, N))
cnt = 0
for i in result:
    limit = 500
    for weight in i:
        limit += weight - K
        if limit < 500:
            break
    else:
        cnt += 1
        
print(cnt)
    
