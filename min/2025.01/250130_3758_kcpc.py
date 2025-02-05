import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 팀 개수, 문제 개수, 내팀id, 로그 엔트리 개수
    n, k, t, m = map(int, input().split())

    # 최종점수 / 제출 횟수 / 최종 제출 시간
    S = [0] * (n+1)
    C = [0] * (n + 1)
    L = [0] * (n + 1)

    # 팀 문제별 점수
    N = [[0] * (k+1) for _ in range(n+1)]

    for a in range(m):
        # 팀 id, 문제번호, 획득한점수
        i, j, s = map(int, input().split())

        if s > N[i][j]:
            S[i] += s - N[i][j]
            N[i][j] = s
        C[i] += 1
        L[i] = a

    team = [(i, S[i], C[i], L[i]) for i in range(1, n+1)]
    team.sort(key=lambda x:(-x[1], x[2], x[3]))

    for r in range(n):
        if team[r][0] == t:
            print(r+1)