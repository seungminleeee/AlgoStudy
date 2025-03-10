N = int(input())
arr = sorted(list(map(int, input().split())))
result = 0
if N % 2 == 0:
    new_arr = []
    new_arr = arr[N // 2:]
    for i in new_arr:
        result += i * 2
else:
    result = arr[N // 2]
    new_arr = []
    new_arr = arr[(N // 2) + 1 :]
    for i in new_arr:
        result += i * 2

print(result)