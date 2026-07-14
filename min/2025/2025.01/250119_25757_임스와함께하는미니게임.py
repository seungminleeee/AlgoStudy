gametype = {'Y': 1, 'F': 2, 'O': 3}

N, game = input().split()
N = int(N)

player = set()
for i in range(N):
    p = input()
    player.add(p)

cnt = len(player) // gametype[game]

print(cnt)