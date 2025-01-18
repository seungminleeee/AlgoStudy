N, game = input().split()
play = {}
for i in range(int(N)):
    id = input()
    if id in play:
        play[id] += 1
    else:
        play[id] = 1

cnt = len(play.keys())

if game == 'Y':
    print(cnt)
elif game == 'F':
    print(cnt // 2)
else:
    print(cnt // 3)