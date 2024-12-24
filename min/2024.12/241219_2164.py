# N = int(input())
#
# arr = []
# for i in range(N):
#     arr.append(i+1)
#
# def func(lst):
#     if len(lst) == 1:
#         return lst[0]
#     lst.pop(0)
#     last = lst.pop(0)
#     lst.append(last)
#     return func(lst)
#
# ans = func(arr)
# print(ans)

from collections import deque

N = int(input())
arr = deque(range(1, N+1))

while len(arr) > 1:
    arr.popleft()
    last = arr.popleft()
    arr.append(last)

print(arr[0])