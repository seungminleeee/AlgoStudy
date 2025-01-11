N, M = map(int, input().split())
word = {}
for i in range(N):
    string = input()
    if len(string) >= M and string in word:
        word[string] += 1
    elif len(string) >= M and string not in word:
        word[string] = 1

result = sorted(word.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
# result = list(word.items())
# result.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in result:
    print(i[0])