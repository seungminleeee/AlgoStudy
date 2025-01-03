# 실3 분수합 
# 인데.. 최대공약수 구하는 방법이 비효울적이래 ㅠㅠ 그래서 찾아봤는데 
# math 모듈의 gcd 최대공약수 구하는 method 사용 할 수 있대 이건 검색해봄 ㅠㅠ~ 

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())
A3 = A1 * B2 + A2 * B1
B3 = B1 * B2 
small_num = min(A3, B3)
num = [1,]
for i in range(2, small_num + 1):
    if A3 % i == 0 and B3 % i == 0:
        num.append(i)
num.sort()
real_num = num[0]
real_A3 = A3 // real_num 
real_B3 = B3 // real_num

print(real_A3, real_B3)

# 새로운 방법 math 활용 
import math

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())
A3 = A1 * B2 + A2 * B1
B3 = B1 * B2 

gcd = math.gcd(A3, B3)

real_A3 = A3 // gcd
real_B3 = B3 // gcd

print(real_A3, real_B3)