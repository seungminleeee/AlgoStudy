import sys
input = sys.stdin.readline

N = int(input())
mara = {}

for i in range(N):
    name = input()
    if name in mara:
        mara[name] += 1
    else:
        mara[name] = 1

for i in range(N - 1):
    name = input()
    mara[name] -= 1

for key, value in mara.items():
    if value == 1:
        print(key)
