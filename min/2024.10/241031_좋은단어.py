N = int(input())
ans = 0
for i in range(N):
    word = input()
    L = len(word)

    arr = []
    for a in range(L):
        if a == 0 or len(arr) == 0:
            arr.append(word[a])
        else:
            if word[a] == arr[-1]:
                arr.pop()
            else:
                arr.append(word[a])

    if len(arr) == 0:
        ans += 1

print(ans)