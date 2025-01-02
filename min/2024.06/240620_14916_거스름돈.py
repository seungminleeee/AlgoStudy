# 메모리 31120	시간 36

N = int(input())

# 2원 개수, 5원 개수
cnt2 = 0
cnt5 = 0

while N>=0:
    # 5로 나눠떨어지면 5 cnt는 5로 나눈 몫
    if N % 5 ==0:
        cnt5 += N//5
        ans = cnt2 + cnt5
        break
    # 5로 나눠떨어질때까지 N에서 2씩 빼고 2 cnt 증가 시키기
    N -= 2
    cnt2 += 1
else:   # 계산 안되면 -1
    ans = -1

print(ans)