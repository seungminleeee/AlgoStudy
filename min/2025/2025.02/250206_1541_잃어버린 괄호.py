S = list(map(str, input().split('-')))

ans = 0
for i in range(len(S)):
    if i == 0:
        if '+' in S[i]:
            K = list(map(int, S[i].split('+')))
            ans += sum(K)
        else:
            ans += int(S[i])
    else:
        if '+' in S[i]:
            K = list(map(int, S[i].split('+')))
            ans -= sum(K)
        else:
            ans -= int(S[i])

print(ans)