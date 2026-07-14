import sys
input=sys.stdin.readline

N, M = map(int, input().strip().split())
tree = list(map(int, input().strip().split()))

start = 0
end = max(tree)
ans = 0

while start <= end:
    H = (start + end) // 2
    total = 0

    for i in range(N):
        if tree[i] > H:
            total += tree[i] - H

    if total >= M:
        ans = H
        start = H + 1
    elif total < M:
        end = H - 1

print(ans)