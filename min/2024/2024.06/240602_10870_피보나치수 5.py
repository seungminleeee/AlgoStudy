import sys; sys.stdin = open('input.txt')

N = int(input())

# arr = [0, 1]
#
# for i in range(2, N+1):
#     fn = arr[0] + arr[1]
#     arr[0] = arr[1]
#     arr[1] = fn
#
# print(arr[1])

arr = [0, 1] + [0]*N

for i in range(2, N+1):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[N])