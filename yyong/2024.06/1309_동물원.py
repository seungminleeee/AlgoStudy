N =int(input())
dp = [0] * 3
dp[0] = dp[1] = dp[2] = 1

for i in range(1, N):
    # 메모리 초과 때문에 필요할때마다 값 갱신하는 방법으로 변경
    dp[0], dp[1], dp[2] = dp[1] + dp[2], dp[0] + dp[2], dp[0] + dp[1] + dp[2]
    print(dp)

print((dp[0] + dp[1] + dp[2]) % 9901)

