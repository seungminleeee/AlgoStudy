"""
[BOJ] 10825번: 국영수 / 실버2
"""
n = int(input())
arr = []
for _ in range(n):
    name, kor, eng, math = map(str, input().split())
    arr.append((str(name), int(kor), int(eng), int(math)))

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(len(arr)):
    print(arr[i][0])