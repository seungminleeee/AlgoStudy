# 흠냐 모르겠어서 문어박사봄 ... dp 어렵당 ㅜㅜ~ 

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(1, N + 1): # p1 ~ pN 까지
    for j in range(1, N + 1): # 카드 1 ~ N장
        if j - i >= 0: # 인덱스 범위
            dp[j] = max(dp[j], dp[j - i] + arr[i])

print(dp[N])

