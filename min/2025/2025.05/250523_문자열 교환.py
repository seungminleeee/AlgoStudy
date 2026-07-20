char = input()
A = char.count('a')
N = len(char)

char *= 2

b_cnt = float('inf')
for i in range(N):
    window = char[i:i+A]
    b_cnt = min(window.count('b'), b_cnt)

print(b_cnt)