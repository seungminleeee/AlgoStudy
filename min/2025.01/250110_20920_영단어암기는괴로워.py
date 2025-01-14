import sys
from collections import Counter
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
words = data[1:]

words_list = [word for word in words if len(word) >= M]

words_cnt = Counter(words_list)
words_set = list(words_cnt.items())

words_set.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, cnt in words_set:
    print(word)