# 백준 1026번 보물
# 너무 쉬운데 ㄱ-.... 
# 메모리 31120 시간 40 
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
result = 0
for i in range(N):
    result += A[i] * B[i]

print(result)