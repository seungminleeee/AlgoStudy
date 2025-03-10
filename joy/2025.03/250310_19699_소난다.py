# ㅜㅜ dfs로 어캐하는겨

from itertools import combinations
import sys
input = sys.stdin.readline


N, M = map(int, input().split()) # N 소들의 수 M 선별할 소의 수
H = list(map(int, input().split()))
arr = list(combinations(H, M))
num = []
for i in arr:
    num.append(sum(i))

prime = []
for i in range(len(num)):
    if num[i] < 2:
        continue
    for j in range(2, num[i]):
        if num[i] % j == 0:
            break
    else:
        prime.append(num[i])

prime = sorted(set(prime))

if len(prime) == 0:
    print(-1)
else:
    print(*prime)