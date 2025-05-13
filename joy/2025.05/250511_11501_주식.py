T = int(input())
for tc in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    money = 0
    
    for price in reversed(prices): 
        if price > max_price:
            max_price = price
        else:
            money += max_price - price
    
    print(money)

