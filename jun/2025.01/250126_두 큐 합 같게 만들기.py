"""
[PGS] 두 큐 합 같게 만들기 / LV2

풀이:
1. 투포인터 사용

시간복잡도:
- O(n) 예상
"""
from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)

    # 무한루프 방지
    limit = len(q1) * 5
    
    total = sum1 + sum2
    target = total // 2

    # 홀수면 불가
    if total % 2 != 0:
        return -1

    cnt = 0
    while sum1 != target and cnt < limit:

        if sum1 > target:
            # q1에서 q2로 이동
            v = q1.popleft()
            sum1 -= v
            q2.append(v)

        else:
            # q2에서 q1으로 이동
            v = q2.popleft()
            sum2 -= v
            q1.append(v)
            sum1 += v

        cnt += 1

    return cnt if sum1 == target else -1