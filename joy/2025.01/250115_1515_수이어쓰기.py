# num = list(map(int, input()))
# print(num)
# N = 0
# for i in range(len(num)):
#     if i == 0 or num[i] > num[i - 1]:
#         N = N + num[i] 
#     elif i != 0 and num[i] <= num[i - 1]:
#         N = 10 * i + num[i]

# print(N)

num = list(map(int, input())) 
N = 0 # 최소 숫자
cur_idx = 0 # 현재인덱스
while cur_idx < len(num):
    N += 1
    for i in str(N): # N 을 증가시키면서
        if cur_idx < len(num) and int(i) == num[cur_idx]: # 인덱스가 num 의 길이보다 작고 i 가 num[cur_idx] 값과 같을 때
            cur_idx += 1 # 인덱스 1 증가시킴

print(N)