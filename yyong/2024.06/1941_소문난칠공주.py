# a형 시험봤을때 게리멘더링 풀었던 방식이랑 똑같이 풀어봄.. -> 시간 안될줄알았는데 되네..!

from collections import deque
from itertools import combinations

classroom = [list(input()) for _ in range(5)]
spot = [(i, j) for i in range(5) for j in range(5)]
# print(spot)
princess_case = 0

# 칠공주 연결됐는지 bfs 확인
def check(arr):
    
    checked = [(arr[0][0], arr[0][1])]
    Q = deque([(arr[0][0], arr[0][1])])

    while Q:
        cx, cy = Q.popleft()

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in checked and (nx, ny) in arr:
                checked.append((nx, ny))
                Q.append((nx, ny))

    return set(checked) == set(arr)

# 칠공주 만들기 조합
for case in combinations(spot, 7):
    member = list(map(lambda x: classroom[x[0]][x[1]], case))
    
    if member.count('S') >= 4 and check(case):
        princess_case += 1

print(princess_case)