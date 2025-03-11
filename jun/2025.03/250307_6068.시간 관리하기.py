"""
[BOJ] 6068번: 시간 관리하기 / 골드5
"""
n = int(input())  # (1<=N<=1000)
arr = []
for _ in range(n):
    t, s = map(int, input().split())  # (1<=T_i<=1,000) / (1<=S_i<=1,000,000)
    arr.append((t, s))
arr.sort(key=lambda x: x[1], reverse=True)

t = arr[0][1]
for s, e in arr:
    if t > e:
        t = e
    t -= s

if t < 0:
    print(-1)
else:
    print(t)