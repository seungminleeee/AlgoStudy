# 실5 팩토리얼 0의 개수 
# 메모리 31120 시간 40 

N = int(input())
num = 1
cnt = 0
for i in range(1, N + 1):
    num *= i

number = str(num)
reverse_number = number[::-1]

for i in reverse_number:
    if i == '0':
        cnt +=1 
    else:
        break 

print(cnt)
