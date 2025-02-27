"""
[PGS] 보석 쇼핑 / 2020 카카오 인턴십
"""
from collections import defaultdict

def solution(gems):
    answer = [0, len(gems)]
    kind_count = len(set(gems))
    gems_count = defaultdict(int)
    left, right = 0, 0

    # 투 포인터 (슬라이딩 윈도우)
    while right < len(gems):
        gems_count[gems[right]] += 1
        right += 1

        while len(gems_count) == kind_count:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]

            gems_count[gems[left]] -= 1
            if gems_count[gems[left]] == 0:
                del gems_count[gems[left]]
            left += 1

    return [answer[0] + 1, answer[1]]