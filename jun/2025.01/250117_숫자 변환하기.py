"""
[PGS] 숫자 변환하기 / LV2

생각:
1. x를 +n, *2, *3 해서 y를 만들어야 함.
2. 처음에 그리디인 것 같아서 계속 고민하다가 모르겠어서 완탐으로 해보기
3. 최단으로 최적 해 구하기 -> bfs ㄱㄱ
"""
from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = set()

    while queue:
        cur, num = queue.popleft()

        if cur == y:
            return num

        if cur in visited:
            continue
        visited.add(cur)

        for i in (cur + n, cur * 2, cur * 3):
            if i <= y and i not in visited:
                queue.append((i, num + 1))

    return -1