import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    apply = [tuple(map(int, input().split())) for _ in range(N)]
    apply.sort()
    
    cnt = 1
    interview = apply[0][1]
    for i in range(1, N):
        if apply[i][1] < interview:
            cnt += 1
            interview = apply[i][1]
    
    print(cnt)
    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    apply = [list(map(int, input().split())) for _ in range(N)]
    apply.sort(key= lambda x: x[0])
    
    cnt = 1
    interview = apply[0][1]

    for i in range(1, N):
        if apply[i][1] < interview:
            cnt += 1
            interview = apply[i][1]
    print(cnt)
