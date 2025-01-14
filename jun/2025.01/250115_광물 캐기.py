"""
[PGS] 광물 캐기 / LV2
"""
def solution(picks, minerals):
    fatigability = [
        [1, 1, 1],  # 다이아
        [5, 1, 1],  # 철
        [25, 5, 1]  # 돌
    ]

    # 곡괭이질 할 수 있는 광물 계산
    ableCount = min(sum(picks) * 5, len(minerals))

    # 5개씩 그룹화해서 비싼광물 많은 순으로 정렬
    groups = []
    for i in range(0, ableCount, 5):
        group = minerals[i:i + 5]
        diamond = group.count("diamond")
        iron = group.count("iron")
        stone = group.count("stone")
        groups.append((diamond, iron, stone))

    groups.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    # 피로도 계산하기
    answer = 0
    for group in groups:
        if sum(picks) == 0:
            break

        for idx in range(3):
            if picks[idx] > 0:
                picks[idx] -= 1
                for i in range(3):
                    answer += group[i] * fatigability[idx][i]
                break

    return answer