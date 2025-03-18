"""
[PGS] 퍼즐 게임 챌린지 / PCCP 기출문제
"""
def is_clear(level, diffs, times, limit):
    n = len(diffs)
    total_time = 0
    time_prev = 0

    for i in range(n):
        diff = diffs[i]
        time_cur = times[i]

        if diff <= level:
            total_time += time_cur
        else:
            count = diff - level
            total_time += (time_cur + time_prev) * count + time_cur

        if total_time > limit:
            return False

        time_prev = time_cur

    return total_time <= limit


def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    answer = float('inf')

    while left <= right:
        mid = (left + right) // 2

        if is_clear(mid, diffs, times, limit):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer