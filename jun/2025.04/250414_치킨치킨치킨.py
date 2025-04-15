"""
[BOJ] 치킨치킨치킨 / 실버4
"""
n, m = map(int, input().split())  # N (1 ≤ N ≤ 30), M (3 ≤ M ≤ 30)
preferences = [list(map(int, input().split())) for _ in range(n)]

max_val = 0
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            total = 0
            for preference in preferences:
                max_preference = max(preference[i], preference[j], preference[k])
                total += max_preference
            max_val = max(max_val, total)

print(max_val)