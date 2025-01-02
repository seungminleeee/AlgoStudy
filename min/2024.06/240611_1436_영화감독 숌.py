# 메모리 31120 / 시간 916
N = int(input())
N = N - 1

arr = []
for num in range(666,10000666):
    st = str(num)
    if '666' in st:
        arr += [num]
    if len(arr) > N:
        break    # 이렇게 하니까 시간 많이 줄음

print(arr[N])


# # 메모리 32528	/ 시간 2324
# N = int(input())
# N = N - 1

# arr = []
# for num in range(666,10000666):
#     st = str(num)
#     if '666' in st:
#         arr += [num]

# print(arr[N])
