N = int(input())
keys = []

for _ in range(N):
    words = list(input().split())

    flag = False
    ret = []
    for W in words:
        if flag:
            ret.append(W)
        elif W[0].upper() not in keys and W[0].lower() not in keys:
            keys.append(W[0])
            flag = True
            ret.append(f'[{W[0]}]{W[1:]}')
        else:
            ret.append(W)

    if flag:
        print(*ret)
    else:
        words = list(str(" ".join(words)))
        L = len(words)
        for i in range(L):
            if words[i] != " " and words[i].upper() not in keys and words[i].lower() not in keys:
                keys.append(words[i])
                words[i] = f'[{words[i]}]'
                break

        print("".join(words))