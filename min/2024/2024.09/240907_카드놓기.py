# 처음에 lst를 리스트로 놓고 하니까 중복제거가 안되서 틀린듯?
# => set으로 바꾸고 하니까 됨~~

from itertools import permutations

N = int(input())
K = int(input())

arr = []
for i in range(N):
    num = input()
    arr.append(num)

lst = set(permutations(arr, K))
ret = []
for j in lst:
    sr = ''.join(j)
    if sr not in ret:
        ret.append(sr)

# ret.sort()
# print(ret)
print(len(ret))
