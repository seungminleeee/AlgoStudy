# N, K = map(int, input().split())
# string = list(input())
# ham = [0 for _ in range(N)]
# cnt = 0
# for i in range(N):
#     if string[i] == 'P':
#         for j in range(max(0, i - K), min(N, i + K + 1)):
#             if string[j] == 'H':
#                 ham[j] = 1
#                 break
# print(ham.count(1))
# print(ham)

        
N, K = map(int, input().split())
string = list(input())
cnt = 0
for i in range(N):
    if string[i] == 'P':
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if string[j] == 'H':
                string[j] = 1
                break
            
print(string.count(1))