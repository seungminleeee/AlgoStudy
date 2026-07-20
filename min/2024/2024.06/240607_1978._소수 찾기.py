import sys; sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

ret = 0
for num in arr:
    lst = []
    for i in range(2,num):
        if num % i == 0:
            lst.append(i)
    if num != 1 and len(lst) == 0:
        ret += 1

print(ret)