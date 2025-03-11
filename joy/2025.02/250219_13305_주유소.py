N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
min_price = price[0] # 기름값싼거 저장
total_price = 0

for i in range(N - 1):
    min_price = min(min_price, price[i]) # 기름값 싼 거로 갱신해줘야함
    total_price += min_price * road[i]

print(total_price)