N = int(input())
level = list(map(int, input().split()))

level.sort(reverse=True)

gold = 0
for i in range(N-1):
    gold += level[i] + level[i+1]
    level[i+1] = level[i]

print(gold)