"""
[BOJ] 25757번: 임스와 함께하는 미니게임 / 실5

조건:
1. 시간 제한 1초
2. 윷놀이(Y) 2명, 같은 그림 찾기(F) 3명, 원카드(O) 4
3. 인원 수가 부족하면 게임시작 불가
4. 사람들이 임스와 함께 플레이 하기를 신청한 횟수 N
5. 최대 몇 번이나 임스와 함께 게임을 플레이 할 수 있는지 구하기
6. 임스는 한 번 같이 플레이 한 사람과는 다시 플레이 하지 않음.
7. 1 <= N <= 100,000
"""
game_player_cnt = 0

n, g = map(str, input().split())

if g == "Y":
    game_player_cnt = 2
elif g == "F":
    game_player_cnt = 3
elif g == "O":
    game_player_cnt = 4

cnt = 0
ans = 0
played = set()
for _ in range(int(n)):
    name = input()

    if name not in played:
        played.add(name)
        cnt += 1

        if cnt == game_player_cnt - 1:
            ans += 1
            cnt = 0

print(ans)