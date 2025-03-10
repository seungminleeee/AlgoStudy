"""
[PGS] 서버 증설 횟수 / LV2
"""
def solution(players, m, k):
    server = [0] * 24
    answer = 0

    for time, player in enumerate(players):
        if player >= m:
            # 필요한 서버 수
            required = (player // m) - server[time]
            if required > 0:
                for i in range(k):
                    if time + i < 24:
                        server[time + i] += required
                answer += required

    return answer