"""
[BOJ] 1940번: 주몽 / 실버4

조건:
1. 시간제한 2초
2. 갑옷을 만드는 재료들은 각각 고유한 번호를 갖고 있음. (중복 번호 없다는 뜻인 것 같음.)
3. 두 개의 재료로 만듦.
4. 두 재료의 합은 1 ~ 10,000,000
5. 재료의 개수는 1 ~ 15,000
6. 몇개의 갑옷을 만들 수 있는가 ? 를 구하는 문제

생각:
1. N(재료의 개수), M(갑옷을 만드는 데 필요한 수), lst(재료 고유 번호)
2. 예시를 보니, lst의 숫자들 중 2개의 합이 M이 되는 개수를 세는 것 같음.

풀이:
1. 이중 for문 사용하면 O(N^2)이 되서 최대 기준 15000^2은 2억번 이상이기에 시간초과 발생
2. 생각이 안나서 알고리즘 분류 확인 후에 투포인터 문제인 것을 확인함.
3. 투포인터로 풀이
"""
N = int(input())
M = int(input())
arr = list(map(int, input().split()))

arr.sort()

ans = 0
cur_sum = 0
left = 0
right = N-1
while left < right:
    cur_sum = arr[left] + arr[right]

    if cur_sum == M:
        ans += 1
        left += 1
        right -= 1
    elif cur_sum < M:
        left += 1
    else:
        right -= 1

print(ans)