import sys
from bisect import bisect_left

input=sys.stdin.readline

N, M = map(int, input().split())
name = []
limit = []
for _ in range(N):
    a, b = input().split()
    name.append(a)
    limit.append(int(b))

for _ in range(M):
    power = int(input())
    idx = bisect_left(limit, power)
    print(name[idx])
