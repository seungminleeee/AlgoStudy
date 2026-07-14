import sys; sys.stdin = open('input.txt')

A, B = map(int, input().split())

mx = 1
for i in range(1, min(A, B)+1):
    if A % i == 0 and B % i == 0:
        mx = i

print(mx)

mn = A * B // mx

print(mn)