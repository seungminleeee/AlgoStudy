import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
name = [input().rstrip() for _ in range(N)]
complete = [input().rstrip() for _ in range(N-1)]

name_cnt = Counter(name)

for c in complete:
    name_cnt[c] -=1

for n in name_cnt:
    if name_cnt[n] > 0:
        print(n)
        break