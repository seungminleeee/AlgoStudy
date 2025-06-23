from collections import Counter

N = int(input())
words = []
words_len = []
for _ in range(N):
    W = list(input())
    words.append(Counter(W))
    words_len.append(len(W))

cnt = 0
word = words[0]
L = words_len[0]
for i in range(1, N):
    temp = words[i].copy()
    diff = 0
    for w in word:
        temp[w] -= word[w]

    for a in temp:
        diff += abs(temp[a])

    if diff <= 1:
        cnt += 1
    elif diff == 2 and L == words_len[i]:
        cnt += 1

print(cnt)