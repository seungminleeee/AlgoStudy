"""
[BOJ] 13305번: 주유소 / 실버3
"""
n = int(input())
roads_length = list(map(int, input().split()))
cities_L_price = list(map(int, input().split()))

min_price = cities_L_price[0]
total = 0

for i in range(n - 1):
    if cities_L_price[i] < min_price:
        min_price = cities_L_price[i]

    total += (min_price * roads_length[i])

print(total)