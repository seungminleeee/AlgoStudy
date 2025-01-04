# 처음에 조합으로 풀었는데 시간초과 남

# 1 (pypy로 했을 때 맞음)
# 리스트 정렬 후 앞에서부터 돌면서 M에서 수를 뺀 값이 리스트에 존재하는지 확인
N = int(input())
M = int(input())
nums = list(map(int,input().split()))
nums.sort()

cnt = 0
for n in nums:
    K = M - n
    # 리스트 뒤에서부터 돌면서 M-n과 같은값이 있는지 확인
    # m이 n보다 작거나 M-n 값보다 작으면 더 찾을 필요 없음
    for m in nums[::-1]:
        if m <= n:
            break

        if m == K:
            cnt += 1
            break
        elif m < K:
            break

print(cnt)

# 2
# 다들 투포인터로 풀어서 다시 풀어봄
N = int(input())
M = int(input())
nums = list(map(int,input().split()))
nums.sort()

L = 0
R = N - 1
cnt = 0

while L < R:
    num_sum = nums[L] + nums[R]
    if num_sum == M:
        cnt += 1
        L += 1
        R -= 1
    elif num_sum < M:
        L += 1
    elif num_sum > M:
        R -= 1

print(cnt)