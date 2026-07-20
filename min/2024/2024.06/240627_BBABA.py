# 메모리31120	시간32

N = int(input())

A = 1   # A의 수
B = 0   # B의 수

for i in range(N):
    Aold = A    # 기존 A 저장하기
    A = B   # A는 이전 B의 개수와 같아짐
    B = B + Aold    # B는 기존 A와 기존 B의 합과 같음

print(A, B)