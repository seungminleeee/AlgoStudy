from collections import defaultdict

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = defaultdict(int)

left = 0
max_len = 0
for right in range(N):
    cnt[arr[right]] += 1

    while cnt[arr[right]] > K:
        cnt[arr[left]] -= 1
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)