P, M = map(int, input().split())
players = []
for _ in range(P):
    level, nickname = input().split()
    players.append((int(level), nickname))

rooms = []
for level, nickname in players:
    placed = False
    for room in rooms:
        if len(room) < M and abs(room[0][0] - level) <= 10:
            room.append((level, nickname))
            placed = True
            break

    if not placed:
        rooms.append([(level, nickname)])

for room in rooms:
    if len(room) == M:
        print('Started!')
    else:
        print('Waiting!')

    room.sort(key=lambda x:x[1])
    for r in room:
        print(*r)