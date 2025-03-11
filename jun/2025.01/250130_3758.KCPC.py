"""
[BOJ] 3758번: KCPC / 실2

조건:
1. 시간 제한 1초
2. 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 더 높음.
3. 점수도 같고, 횟수도 같을 경우 제출시간 빠른 순으로
4. 테스트 데이터의 수 T, 팀의 개수 n, 문제 개수 k, 팀 id t, 로그 엔트리 개수 m
5. id i, 문제 번호 j, 획득 점수 s
"""
T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    scores = [[0] * (k + 1) for _ in range(n + 1)]
    count = [0] * (n + 1)
    last_time = [0] * (n + 1)
    for time in range(1, m + 1):
        i, j, s = map(int, input().split())
        scores[i][j] = max(scores[i][j], s)
        count[i] += 1
        last_time[i] = time

    team_ranks = []
    for team_id in range(1, n + 1):
        total_score = sum(scores[team_id])
        team_ranks.append((total_score, count[team_id], last_time[team_id], team_id))
    team_ranks.sort(key=lambda x: (-x[0], x[1], x[2]))

    for rank, team in enumerate(team_ranks, start=1):
        if team[3] == t:
            print(rank)
            break