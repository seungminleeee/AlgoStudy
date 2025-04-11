n = int(input())
wine = [0] + list(int(input()) for _ in range(n))

prev_0, prev_1, prev_2 = 0, wine[1], 0

for i in range(2, n+1):


    cur_0 = max(prev_0, prev_1, prev_2)
    cur_1 = prev_0 + wine[i]
    cur_2 = prev_1 + wine[i]
    
    # 이전 상태 갱신
    prev_0, prev_1, prev_2 = cur_0, cur_1, cur_2


print(max(prev_0, prev_1, prev_2))