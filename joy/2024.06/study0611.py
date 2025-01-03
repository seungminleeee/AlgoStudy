# 6/11 study 문제 메모리 31120 시간 964
# 백준 실5 1436번 영화감독 숌 

N = int(input())
num = 666 
cnt = 0

while cnt <= N: #cnt 가 N 보다 같거나 작을때까지 반복
    if '666' in str(num): # num에 666이 들어있으면 
        cnt += 1 # cnt 1 증가 
    if cnt == N: # 만약에 cnt 가 N이랑 같이진다면 
        print(num) # num 출력 하고 반복문 탈출
        break 
    else: # 둘 다 아니라면 num 숫자를 증가시킴 666-> 667 -> ... -> 1666 -> 1667 -> ... -> 6660 -> 6661 이런식으로 
        num += 1
