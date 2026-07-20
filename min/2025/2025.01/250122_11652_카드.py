from collections import Counter

import sys
input = sys.stdin.readlines


data = list(map(int, input()))
N = data[0]
count = Counter(data[1:])

max_count = max(count.values())
nums = []

for c in count:
    if count[c] == max_count:
        nums.append(c)

print(min(nums))