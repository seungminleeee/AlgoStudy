"""
[BOJ] 비슷한 단어 / 실버2
"""
from collections import Counter

n = int(input())
word = input()
length = len(word)
ans = 0

word_counter = Counter(word)

for _ in range(n - 1):
    next_word = input()
    next_counter = Counter(next_word)

    diff = 0

    chars = set(word_counter) | set(next_counter)

    for char in chars:
        diff += abs(next_counter[char] - word_counter[char])

    if diff == 0:
        ans += 1
    elif diff == 1:
        ans += 1
    elif diff == 2 and len(word) == len(next_word):
        ans += 1

print(ans)