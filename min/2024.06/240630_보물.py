# 메모리 31120  시간 48

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

S = 0
for i in range(N):
    a = A.pop()
    b = B.pop()
    S += a*b

print(S)