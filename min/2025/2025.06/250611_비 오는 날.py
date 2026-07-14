T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())

    if M == 1 and K == 1 and N > 1:
        print(-1)
        continue

    cnt = 0
    remain = N

    while remain > 0:
        cnt += 1
        remain -= min(M*K, remain)

        if remain == 0:
            break
        
        remain += 1
        cnt += 1

    print(cnt if cnt else -1)