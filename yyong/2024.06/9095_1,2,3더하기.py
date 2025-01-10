# 걍 수열 문제인듯.. swea 종이 붙이기 같은...

dp = [0] * 12

dp[0] = dp[1] = 1
dp[2] = 2

def plus(num):

    if not dp[num]:
        dp[num] = plus(num-1) + plus(num-2) + plus(num-3)
    
    return dp[num]

for _ in range(int(input())):

    num = int(input())

    print(plus(num))