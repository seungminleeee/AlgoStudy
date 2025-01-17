N = int(input()) # 공이 들어간 횟수
arr = [] # 팀 - 초로 변환한 시간 튜플 들어갈 배열 

for _ in range(N):
    team, time = input().split()
    minutes, seconds = map(int, time.split(':'))
    total_seconds = 60 * minutes + seconds
    arr.append((int(team), total_seconds))
    
one_score, two_score = 0, 0 # 팀의 스코어를 담는 변수
one_time, two_time = 0, 0 # 이긴 시간 담는 변수
last_time = 0 # 지속 시간
lead_team = 0 # 리드 팀

for team, time in arr: 
    if lead_team == 1:  
        one_time += time - last_time 
    elif lead_team == 2: 
        two_time += time - last_time
    
    if team == 1:
        one_score += 1
    else:
        two_score += 1
    
    if one_score > two_score:
        lead_team = 1
    elif one_score < two_score:
        lead_team = 2
    else:
        lead_team = 0
    
    last_time = time

if lead_team == 1:
    one_time += 2880 - last_time
elif lead_team == 2:
    two_time += 2880 - last_time

one_minute = one_time // 60
one_second = one_time % 60
two_minute = two_time // 60
two_second = two_time % 60

print(f"{one_minute:02}:{one_second:02}")
print(f"{two_minute:02}:{two_second:02}")