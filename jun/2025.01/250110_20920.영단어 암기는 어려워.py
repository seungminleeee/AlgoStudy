"""
[BOJ] 20920번: 영단어 암기는 어려워 / 실3

조건:
1. 시간 제한 1초
2. 자주 나오는 단어 일수록 앞에 배치
3. 단어의 길이가 길수록 앞에 배치
4. 알파벳 사전 순으로 앞에 있는 단어 일수록 앞에 배치
5. M 이상인 단어만
6. 1 <= N <= 100,000 / 1 <= M <= 10

생각:
1. Counter로 개수 세서 구현으로 풀어볼 생각
2. 시간 복잡도는 중복단어가 없다치면 O(N*log^N)인데 중복이 있기에 더 줄어들 예정
3. 이 문제는 복잡도 게산 복잡하네요.. 단어길이, 필터링된 단어 개수의 리스트 등등 많다..

풀이:
1. 카운터로 개수세서 필터링하고
2. 람다식으로 정렬기준 세워서 만들고 출력
3. 문제 밑에 sys랑 rstrip 쓰라고 나오는데, 첨에 시간초과 떴다가 이거 해주니까 맞음.(이런거 없어야하는데 ;)
"""
import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
word = Counter(input().rstrip() for _ in range(n))

filter_word = [(k, v) for k, v in word.items() if len(k) >= m]
filter_word.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for ans, _ in filter_word:
    print(ans)