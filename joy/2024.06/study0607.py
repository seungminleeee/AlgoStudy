# 1978번 소수 찾기 
N = int(input())
arr = map(int, input().split())
prime_cnt = 0
for i in arr:
    if i == 1:
        continue
    elif i == 2:
        prime_cnt += 1
    else:
        prime_check = True
        for j in range(2, i):
            if i % j == 0:
                prime_check = False 
                break 
        if prime_check == True:
            prime_cnt += 1

print(prime_cnt)
