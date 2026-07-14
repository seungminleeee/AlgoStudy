import sys; sys.stdin = open('input.txt')

N = 3

T = int(input())
for i in range(T):
    arr = list(map(int, input().split()))

    new_arr = []

    for j in range(N):
        new_arr.append(max(arr))
        arr.remove(max(arr))
    print(new_arr[-1])