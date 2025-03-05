"""
[BOJ] 19699번: 소-난다! / 실버2
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def dfs(start, count, total):
    if count == m and is_prime(total):
        answers.add(total)
        return

    for i in range(start, n):
        dfs(i + 1, count + 1, total + weights[i])

n, m = map(int, input().split())  # 1 <= m <= n <= 9
weights = list(map(int, input().split()))

answers = set()
dfs(0, 0, 0)

if answers:
    print(*sorted(answers))
else:
    print(-1)