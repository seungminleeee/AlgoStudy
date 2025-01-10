# 9625번 BABBA 실5
# 메모리 31120 시간 36
K = int(input())
A = 1
B = 0
for i in range(K): 
    A, B = B, B + A

print(A, B)

# 실패 버전 ..... 이상하네 
# K = int(input())
# string = 'A'
# for i in range(K):
#     for j in string:
#         if j == 'A':
#             string = 'B'
#         elif j == 'B':
#             string = 'BA'

# A_check = string.count('A')
# B_check = string.count('B')

# print(A_check, B_check)
