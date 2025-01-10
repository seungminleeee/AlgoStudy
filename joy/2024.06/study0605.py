# 백준 1292번 쉽게 푸는 문제
num1, num2 = map(int, input().split())
arr = []
for i in range(1, 200):
    arr = arr + [i] * i

print(sum(arr[num1 - 1:num2]))
