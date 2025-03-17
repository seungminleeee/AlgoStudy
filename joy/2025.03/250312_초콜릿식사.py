import math, sys
input = sys.stdin.readline

K = int(input())
min_choco = 2 ** math.ceil(math.log2(K)) # 2^x >= K -> x >= log2(K)
remain = min_choco
cnt = 0

while remain:
    if K % remain == 0:
        break
    remain = remain // 2
    cnt += 1

# while K > 0:
#     half = remain // 2
#     if half <= K:
#         K -= half
#     remain = half
#     cnt += 1
        

print(min_choco, cnt)