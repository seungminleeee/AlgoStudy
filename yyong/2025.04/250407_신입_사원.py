for _ in range(int(input())):

    N = int(input())
    candidate = [list(map(int, input().split())) for _ in range(N)]

    candidate.sort()

    candidate_count = 1
    grade = candidate[0][1]  # 뒤 후보들은 무조건 이 등수보다 높아야함

    for i in range(1, N):

        if grade > candidate[i][1]:
            candidate_count += 1
            grade = candidate[i][1]  # 이 등수보다 잘나야하므로 기준값 갱신

    print(candidate_count)