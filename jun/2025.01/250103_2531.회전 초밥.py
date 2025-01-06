"""
[BOJ] 2531번: 회전 초밥 / 실버1

조건:
1. 시간제한 1초
2. 같은 종류의 초밥 둘 이상 있을 수 있음.
3. 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
4. 초밥의 종류 하나가 쓰인 쿠폰 발행 -> 위 행사에 참여할 경우 쿠폰에 적힌 초밥 하나는 무료로 제공
IF 없을 경우 새로 만들어 제공 (위 행사에 참여할 경우를 조심)
5. INPUT(벨트에 놓인 접시 수 N, 초밥 가짓 수 d, 연속해서 먹는 접시의 개수 k, 쿠폰 번호 c)
6. 손님이 먹을 수 있는 초밥 가짓 수의 최대 값 구하기
7. N 최대 30,000 / d 최대 3,000 / k 최대 3,000

생각:
1. 초밥 리스트에 다 넣고 0번부터 연속으로 쭉 돌려볼 생각 (시간복잡도 O(n*k) 예상)
2. 연속으로 해서 set에 넣고 마지막에 쿠폰번호도 넣고, 개수 세서 최대값 구해볼 생각

풀이:
1. O(n*k)로 9천만 나와서 실버 문제라 1초 안될줄 알았는데, 시간초과가 나왔음. set 때문에 시간 더 들어서.
2. 슬라이딩 윈도우로 풀어서 시간복잡도 O(n) 으로 해서 풀어야 할듯 함.
"""
from collections import defaultdict

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]

sushi_dict = defaultdict(int)
unique_cnt = 0
max_cnt = 0

for i in range(k):
    if sushi_dict[belt[i]] == 0:
        unique_cnt += 1
    sushi_dict[belt[i]] += 1

max_cnt = unique_cnt + (1 if sushi_dict[c] == 0 else 0)

for i in range(N):
    new_sushi = belt[(i+k) % N]
    if sushi_dict[new_sushi] == 0:
        unique_cnt += 1
    sushi_dict[new_sushi] += 1

    old_sushi = belt[i]
    sushi_dict[old_sushi] -= 1
    if sushi_dict[old_sushi] == 0:
        unique_cnt -= 1

    max_cnt = max(max_cnt, unique_cnt + (1 if sushi_dict[c] == 0 else 0))

print(max_cnt)