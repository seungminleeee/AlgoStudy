"""
[BOJ] 21921번: 블로그 / 실3

조건:
1. x일 동안 가장 많은 방문자 수 구하기
2. 0이라면 SAD 출력
3. 1 <= x <= n <= 250,000
4. 0 <= 방문자 수 <= 8,000
"""
def solve(n, x, visits):
    cur_sum = sum(visits[:x])
    max_sum = cur_sum
    max_cnt = 1
    for i in range(x, n):
        cur_sum += visits[i]
        cur_sum -= visits[i - x]
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_cnt = 1
        elif cur_sum == max_sum:
            max_cnt += 1
    if max_sum == 0:
        print("SAD")
    else:
        print(max_sum)
        print(max_cnt)

n, x = map(int, input().split())
visits = list(map(int, input().split()))
solve(n, x, visits)