N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]

meeting.sort(key=lambda x:(x[1], x[0]))

meeting_count = 1
last_time = meeting[0][1]

for i in range(1, N):
    
    if last_time <= meeting[i][0]:
        meeting_count += 1
        last_time = meeting[i][1]

print(meeting_count)