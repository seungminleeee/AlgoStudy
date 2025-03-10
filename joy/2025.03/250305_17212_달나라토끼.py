N = int(input())
coin = [1, 2, 5, 7]
result = [float('inf')] * (N + 1)
result[0] = 0

for i in range(1, N + 1):
    for c in coin:
        if i >= c:
            result[i] = min(result[i], result[i - c] + 1)

print(result[N])