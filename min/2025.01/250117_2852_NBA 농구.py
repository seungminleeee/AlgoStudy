N = int(input())
lst = []

for i in range(N):
    st = input()
    lst.append(st)

cnt = [0, 0, 0]
Time = [0, 0, 0]

last = 0
finish = 48 * 60

for i in range(N):
    team, goal = lst[i].split()
    team = int(team)
    min, sec = map(int, goal.split(':'))
    time = min*60 + sec

    if cnt[1] > cnt[2]:
        Time[1] += time - last
    elif cnt[2] > cnt[1]:
        Time[2] += time - last


    last = time
    cnt[team] += 1

if cnt[1] > cnt[2]:
    Time[1] += finish - last
elif cnt[2] > cnt[1]:
    Time[2] += finish - last


result1 = str(Time[1] // 60).zfill(2) + ":" + str(Time[1] % 60).zfill(2)
result2 = str(Time[2] // 60).zfill(2) + ":" + str(Time[2] % 60).zfill(2)

print(result1)
print(result2)