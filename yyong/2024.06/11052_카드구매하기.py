N = int(input())
cards = [0] + list(map(int, input().split()))  # 인덱스 i + 1 = 카드 수, cards[i] = 카드팩 가격
dp = [0] * (N+1)

# 카드 한개 구매할때, 두개 구매할때 ,... N개 구매할때까지 카드 수 늘려가면서 계산하기
for i in range(1, N + 1):
    for j in range(1, i + 1):
        # dp[i-j] (카드 j장 빼고) + cards[j] (카드j장 묶인 카드팩 넣기)
        # -> 이걸 자꾸 dp[i-1]에서 가져온 다음에 가공하려니까 힘들었음 ㅠ 
        dp[i] = max(dp[i], dp[i - j] + cards[j])

# print(dp)
print(dp[N])