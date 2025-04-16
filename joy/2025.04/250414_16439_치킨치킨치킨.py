from itertools import combinations

N, M = map(int, input().split())
chicken = [list(map(int, input().split())) for _ in range(N)]
lst = [i for i in range(M)]
max_result = 0
comb = list(combinations(lst, 3))
for com in comb: # 치킨 조합
    result = 0
    for i in range(N): # 사람
        best = 0
        for j in com: # 고를 수 있는 치킨 종류 
            best = max(best, chicken[i][j]) # 가장 높은 점수 저장
        result += best
    max_result = max(max_result, result)

print(max_result)
    