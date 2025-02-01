import sys
sys.stdin=open('input.txt')

input = sys.stdin.readline

N, X = map(int, input().split())
nums = list(map(int, input().split()))

# 누적 합
arr = [0] * N

arr[0] = nums[0]
for i in range(1, N):
    arr[i] = arr[i-1] + nums[i]

# 구간 합
mx = [0] * (N)

for j in range(N):
    if j-X < 0:
        mx[j] = arr[j]
    else:
        mx[j] = arr[j] - arr[j-X]

ans = max(mx)
if ans != 0:
    print(ans)
    cnt = mx.count(ans)
    print(cnt)
else:
    print("SAD")
