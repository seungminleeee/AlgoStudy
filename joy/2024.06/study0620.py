# 실5 거스름돈 
# 메모리 31120 시간 40

n = int(input())
money = 0
while n >= 0: # n 이 0보다 크거나 같을때까지
    if n % 5 == 0: # 그러다가 5로 나누어지는 수가 나오면 
        money += n // 5 # 돈에 5로 나눈 몫을 더해줌 
        print(money) # 프린트하고 브레이크
        break
    n -= 2 # -2 씩 빼주면서 
    money += 1 # money 를 하나씩 올려줌
else:
    print(-1)