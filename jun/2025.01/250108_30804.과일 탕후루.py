"""
[BOJ] 30804번: 과일 탕후루 / 실버2

조건:
1. 시간 제한 2초
2. 과일의 종류에는 1~9의 번호 붙어있음.
3. 앞에서 a개, 뒤에서 b개 과일을 빼서 만들 수 있는 과일의 개수가 가장 많은 탕후루 과일 개수 세기
단, 과일은 두 종류 이하
4. 1 <= N <= 200,000

생각:
1. 앞에서 a개, 뒤에서 b개 과일을 빼고 하는거 보니 투포인터처럼 풀면 될듯 함.
2. 딕셔너리에 과일 세면서 두 종류 이상되면 앞에꺼부터 없애면서 가보자

풀이:
1. 꽤나 방법찾는데 오래걸렸다.
2. 특히, right-left+1 이게 맞는지는 모르겠으나, 이거 찾느라 애먹었다.
3. Counter로 날먹하는 방법 써봤는데 거침없이 틀려버렸다. 까비.
"""
from collections import defaultdict

n = int(input())
fruit = list(map(int, input().split()))

left = 0
max_length = 0
count = defaultdict(int)

for right in range(n):
    count[fruit[right]] += 1

    while len(count) > 2:
        count[fruit[left]] -= 1
        if count[fruit[left]] == 0:
            del count[fruit[left]]
        left += 1

    max_length = max(max_length, right-left+1)

print(max_length)