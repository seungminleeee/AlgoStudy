N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

if N == 1:
    print(arr[0])
elif N == 2:
    print(max(arr[1], arr[0] + arr[1]))
else:
    dp = [0] * N
    dp[0] = arr[0] # 첫번째 계단
    dp[1] = arr[0] + arr[1] # 첫번째에서 그 다음꺼도 올라갔을떄
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2]) # 1 - 3 / 2 - 3

    for i in range(3, N):
        dp[i] = max(dp[i-2], dp[i-3] + arr[i-1]) + arr[i] 

    print(dp[-1])