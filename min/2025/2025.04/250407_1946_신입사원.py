import sys
input=sys.stdin.readline

TC = int(input().strip())
for tc in range(TC):
    N = int(input().strip())
    employee = [list(map(int, input().strip().split())) for _ in range(N)]
    employee.sort(key=lambda x:x[0])

    min_interview = employee[0][1]
    cnt = 1
    for i in range(1, N):
        if employee[i][1] < min_interview:
            min_interview = employee[i][1]
            cnt += 1

    print(cnt)