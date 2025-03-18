"""
[BOJ] 1717번: 집합의 표현 / 골드5
"""
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a

n, m = map(int, input().split())
parent = list(range(n + 1))

for _ in range(m):
    check, a, b = map(int, input().split())

    if check == 0:
        union(a, b)

    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')