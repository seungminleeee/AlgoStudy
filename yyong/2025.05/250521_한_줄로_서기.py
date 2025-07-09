N = int(input())
arr = list(map(int, input().split()))
result = [0] * N

for i in range(N):  # 0번 인덱스(1번 사람)부터 돌면서 제자리 찾기
    cnt = 0
    other = 0
    if arr[i] == 0:
        result[result.index(0)] = i+1
    else:
        for j in range(N):
            if result[j] == 0:
                cnt += 1
            else:
                other += 1
            if arr[i] == cnt:
                cur = j+1
                while True:
                    if result[cur]:
                        cur += 1
                    else:
                        break
                result[cur] = i+1
                break

print(*result)