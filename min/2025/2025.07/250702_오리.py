S = list(input())
duck = ['q','u','a','c','k']
progress = []
cnt = 0

for s in S:
    found = False
    for i in range(len(progress)):
        if duck[progress[i]] == s:
            progress[i] += 1
            found = True
            if progress[i] == 5:
                progress[i] = -1
            break
    if not found:
        if s == 'q':
            progress.append(1)
        else:
            print(-1)
            exit()

    progress = [p for p in progress if p != -1]
    cnt = max(cnt, len(progress))

for p in progress:
    if p != 0:
        cnt = -1
        break

if progress:
    print(-1)
else:
    print(cnt)